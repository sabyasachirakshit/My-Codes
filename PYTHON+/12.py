# Print calendar of a given month and year

# Program-

import calendar
month = int(input("Enter Month (number format): "))
year = int(input("Enter Year (number format):"))
print(
    f"The Calendar of month {month} of year {year} is displayed below:\n\n{calendar.month(year,month)}")
