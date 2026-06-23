#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py
Author: "Vidhi Patel"
Semester: "Summer 2026"
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]

def leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    if month == 2:
        return 29 if leap_year(year) else 28
    month_days = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    return month_days[month]

def after(date: str) -> str:
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    day += 1

    if day > mon_max(month, year):
        day = 1
        month += 1

    if month > 12:
        month = 1
        year += 1

    return f"{year}-{month:02}-{day:02}"

def usage():
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")

def valid_date(date: str) -> bool:
    try:
        parts = date.split('-')
        if len(parts) != 3:
            return False
        if len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
            return False

        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])

        if month < 1 or month > 12:
            return False
        if day < 1 or day > mon_max(month, year):
            return False

        return True
    except:
        return False

def day_count(start_date: str, stop_date: str) -> int:
    weekend_days = 0
    current = start_date

    while current <= stop_date:
        year, month, day = current.split('-')
        dow = day_of_week(int(year), int(month), int(day))

        if dow == 'sat' or dow == 'sun':
            weekend_days += 1

        current = after(current)

    return weekend_days

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
        sys.exit()

    date1 = sys.argv[1]
    date2 = sys.argv[2]

    if not valid_date(date1) or not valid_date(date2):
        usage()
        sys.exit()

    start_date, stop_date = sorted([date1, date2])
    weekends = day_count(start_date, stop_date)

    print(f"The period between {start_date} and {stop_date} includes {weekends} weekend days")
