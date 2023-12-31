import math
from datetime import date
import re

def is_valid(birthdate: str):
    regex = r"^([a-z]{3,9})\s([0-2]?[0-9]|3[0-1]),\s?([0-9]{4})$"
    matches = re.match(regex, birthdate, re.IGNORECASE)
    if matches:
        return month_to_integer(matches.group(1)), int(matches.group(2)), int(matches.group(3))
    else:
        raise ValueError("Invalid Date Format.")

def month_to_integer(month: str):
    months = {
        "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
        "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12
    }
    return months.get(month.lower(), 0)

def calculate_age(birthmonth: int, birthday: int, birthyear: int, today):
    total_age = today.year - birthyear
    if birthmonth > today.month or (birthmonth == today.month and birthday > today.day):
        total_age -= 1
    return total_age

def calculate_days(birthmonth: int, birthday: int, today):
    year_birthday = date(today.year, birthmonth, birthday)
    if year_birthday < today:
        year_birthday = year_birthday.replace(year=today.year + 1)
    time_to_birthday = (year_birthday - today).days
    return time_to_birthday

def moon_phase_on_date(year, month, day):
    year_corrected = year
    month_corrected = month
    if month_corrected < 3:
        year_corrected -= 1
        month_corrected += 12
    year_corrected //= 100
    correction = 2 - year_corrected + year_corrected // 4
    JD = math.floor(365.25 * (year + 4716)) + math.floor(30.6001 * (month + 1)) + day + correction - 1524.5
    phase = (JD - 2451550.1) / 29.53058867
    phase = phase - math.floor(phase)
    phase_name = "🌑 New Moon 🌑" if 0.0 <= phase < 0.03 else "🌒 Waxing Crescent 🌒" if 0.03 <= phase < 0.22 else "🌓 First Quarter 🌓" if 0.22 <= phase < 0.28 else "🌔 Waxing Gibbous 🌔" if 0.28 <= phase < 0.47 else "🌕 Full Moon 🌕" if 0.47 <= phase < 0.53 else "🌖 Waning Gibbous 🌖" if 0.53 <= phase < 0.72 else "🌗 Last Quarter 🌗" if 0.72 <= phase < 0.78 else "🌘 Waning Crescent 🌘"
    return phase_name

def main():
    while True:
        print("\033[96;2;255;192;203m")
        birthdate = input("Enter the name of the month, day and year of your birth. (For example: May 16, 1988): ")
        birthmonth, birthday, birthyear = is_valid(birthdate)
        today = date.today()
        age = calculate_age(birthmonth, birthday, birthyear, today)
        days = calculate_days(birthmonth, birthday, today)
        print(f"Your age as of {date.today().strftime('%B %d, %Y')} is {age} years old.\n{days} days before your Birthday!")

        year = int(input("Enter the year number to get information about the Moon phase: "))
        month = int(input("Enter the month number to get information about the Moon phase: "))
        day = int(input("Enter the day number to get information about the Moon phase: "))

        phase = moon_phase_on_date(year, month, day)
        print(f"The Moon phase on the specified date: {phase}")

        restart = input("\nDo you want to run the program again? (yes/no): ")
        if restart.lower() != "yes":
            break

if __name__ == "__main__":
    main()

