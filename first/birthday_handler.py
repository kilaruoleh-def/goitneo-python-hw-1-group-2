from datetime import datetime
from typing import List, Dict


def is_leap_year(year: int) -> bool:
    """
    Check if a given year is a leap year.

    Args:
    - year (int): Year to check.

    Returns:
    - bool: True if leap year, False otherwise.
    """
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


def get_birthdays_per_week(users: List[Dict[str, datetime.date]]) -> None:
    """
    Prints the list of users who have birthdays in the upcoming week.

    Args:
    - users (List[Dict[str, datetime.date]]): List of user dictionaries containing 'name' and 'birthday' keys.

    Returns:
    - None: Outputs to console.
    """
    days_mapping = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    today = datetime.today().date()

    birthdays_per_week = {day: [] for day in days_mapping}

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        # Handling the special case for February 29th
        if birthday.month == 2 and birthday.day == 29 and not is_leap_year(today.year):
            birthday_this_year = birthday.replace(day=28, year=today.year)
        else:
            birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            if birthday.month == 2 and birthday.day == 29 and not is_leap_year(today.year + 1):
                birthday_this_year = birthday.replace(day=28, year=today.year + 1)
            else:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days < 7:
            day_of_week_index = birthday_this_year.weekday()
            # If it's a weekend, move to Monday
            if day_of_week_index >= 5:
                day_of_week_index = 0
            day_of_week = days_mapping[day_of_week_index]
            birthdays_per_week[day_of_week].append(name)

    for day, names in birthdays_per_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")


if __name__ == '__main__':
    sample_users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 16)},
        {"name": "Jill Valentine", "birthday": datetime(1974, 10, 19)},
        {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
        {"name": "Jan Koum", "birthday": datetime(1976, 10, 14)},
        {"name": "John Doe", "birthday": datetime(1990, 10, 17)},
        {"name": "Leap Year Person", "birthday": datetime(2000, 2, 29)}
    ]
    get_birthdays_per_week(sample_users)
