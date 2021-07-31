import fractions


def get_required_water_intake(weight: int) -> float:
    """Takes weight in pounds as an integer, and calculates the minimum amount of water intake necessary
for semi-sustainable health as a float, in ounces, rounded to two decimal spaces"""
    ounces = float(fractions.Fraction(numerator=2, denominator=3) * weight)
    return round(number=ounces, ndigits=2)


def ounces_to_liters(ounces: float) -> float:
    """Converts ounces (float) to liters (float), rounded to two decimal spaces"""
    return round(number=ounces/33.814, ndigits=2)


