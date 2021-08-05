import fractions
import aiosqlite


async def get_required_water_intake(weight: int) -> float:
    """Takes weight in pounds as an integer, and calculates the minimum amount of water intake necessary
for semi-sustainable health as a float, in ounces, rounded to two decimal spaces"""
    ounces = float(fractions.Fraction(numerator=2, denominator=3) * weight)
    return round(number=ounces, ndigits=2)


# TODO: Learn formula directly for weight into liters instead of this nonsense
async def ounces_to_liters(ounces: float) -> float:
    """Converts ounces (float) to liters (float), rounded to two decimal spaces"""
    return round(number=ounces / 33.814, ndigits=2)


# changing this function and the DB structure increased the chance of division by 0 greatly. Work on this.
# also it looks ugly now. There is a simpler way. Take out time to find it.
# instead of calculating the days each time, maybe start updating the days in the DB automatically,
# maybe on a time interval? Also, why convert everything to float at some point to convert back to int? plsfix
async def get_totals() -> tuple:
    """Returns the total water supply in liters, stored weight in pounds, and time in days one could survive
     from an sqlite3 DB"""
    async with aiosqlite.connect("api/water.db") as db:
        cursor = await db.execute("SELECT liters, weight FROM watersupply")
        liters_weight = await cursor.fetchone()
        water_ounces = await get_required_water_intake(weight=liters_weight[1])
        liter = await ounces_to_liters(ounces=water_ounces)
        days = await calculate_days(int(liter), liters_weight[0])
        return liters_weight[0], liters_weight[1], int(days)


async def update_water_amount(new_liters: int) -> str:
    """Allows one to change the amount of water in liters stored in the DB"""
    async with aiosqlite.connect("api/water.db") as db:
        try:
            await db.execute("UPDATE watersupply SET liters = ?", (new_liters,))
            await db.commit()
        except aiosqlite.Error as e:
            new_liters = e
        return str(new_liters)


async def update_weight(new_weight: int) -> str:
    """Allows one to change the weight in pounds stored in the DB"""
    async with aiosqlite.connect("api/water.db") as db:
        try:
            await db.execute("UPDATE watersupply SET weight = ?", (new_weight,))
            await db.commit()
        except aiosqlite.Error as e:
            new_weight = e
        return str(new_weight)


# sometimes causes div/0 errors, find a suitable solution
async def calculate_days(water_required: int, water_total: int) -> int:
    days = water_total/water_required
    async with aiosqlite.connect("api/water.db") as db:
        await db.execute("UPDATE watersupply SET days = ?", (days,))
    return int(days)
