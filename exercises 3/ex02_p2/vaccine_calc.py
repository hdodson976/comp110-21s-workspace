"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730142451"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    remaining_days: int = days_to_target(population, doses, doses_per_day, target)
    # TODO 4: Call future_date and store result in a variable.
    final_date: str = future_date(remaining_days)
    # TODO 5: Print the expected output using the variables above.
    first_half: str = "We will reach " + str(target) + "% vaccination in " + str(remaining_days) + " days,"
    second_half: str = " which falls on " + final_date.strftime("%B %d, %Y") + "."
    print(first_half + second_half)


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """"Uses input to calculate the days needed to reach the target percentage.""""
    percent_of_pop: float = float(population) * (float(target) / 100)
    numerator: float = (percent_of_pop - (float(doses) / 2)) * 2
    enitre_calc: float = numerator / float(doses_per_day)
    rounded: int = round(enitre_calc)
    return rounded


# TODO 3: Define future_date function
def future_date(remaining_days: int) -> str:
    """Calculates the final date"""
    today: datetime = datetime.today()
    remaining: timedelta = timedelta(remaining_days)
    end_date: datetime = today + remaining
    return end_date


if __name__ == "__main__":
    main()
