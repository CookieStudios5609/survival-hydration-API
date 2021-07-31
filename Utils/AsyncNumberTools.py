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


async def get_total_water_supply() -> int:
    """Returns the total water supply in liters from an sqlite3 DB"""
    async with aiosqlite.connect("api/water.db") as db:
        cursor = await db.execute("SELECT * FROM watersupply")
        liters = await cursor.fetchone()
        return int(liters[0])


async def update_water_amount(new_liters: int) -> str:
    """Allows one to change the amount of water in liters stored in the DB"""
    async with aiosqlite.connect("api/water.db") as db:
        try:
            await db.execute("UPDATE watersupply SET liters = ?", (new_liters,))
            await db.commit()
        except aiosqlite.Error as e:
            new_liters = e
        return str(new_liters)
