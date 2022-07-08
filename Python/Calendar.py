"""
? The objective of this python program is to display a calendar of any year user wants to display
"""
import calendar
print('For Watching the dates of B.C year, put a - sign before the year...')
year = int(input('Enter Year:'))
print(f'Calendar of year {year} is displayed below--->')
print(calendar.calendar(year))
print('\nHit Enter to End.......')
input()
