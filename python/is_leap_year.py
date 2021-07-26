def leap_year(year):
    """Determinates if a year is leap"""
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True