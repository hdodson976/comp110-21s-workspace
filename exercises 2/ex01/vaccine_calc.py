"""A vaccination calculator."""

__author__ = "730142451"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: str = input("Population: ")
doses_admin: str = input("Doses administered: ")
doses_per_day: str = input("Doses per day: ")
target_percent: str = input("Target percent vaccinated: ")

per_pop: float = float(population) * (float(target_percent) / 100)
numerator: float = (per_pop - (float(doses_admin) / 2)) * 2
enitre_calc: float = numerator / float(doses_per_day)
rounded: int = round(enitre_calc)

today: datetime = datetime.today()
remaining_days: timedelta = timedelta(rounded)
end_date: datetime = today + remaining_days

first_half: str = "We will reach " + str(target_percent) + "% vaccination in " + str(rounded) + " days,"
second_half: str = " which falls on " + end_date.strftime("%B %d, %Y") + "."

print(first_half + second_half)
