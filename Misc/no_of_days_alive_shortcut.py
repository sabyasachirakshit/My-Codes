from datetime import date
dob = input(
    "Enter Your Date Of Birth in the given format(Date/Month/Year, for ex. 01/January/2012) : ")
current_date = input(
    "\nEnter Current Date in the given format(Date/Month/Year, for ex. 13/March/2022) : ")
dd = 0
mm = 0
yy = 0
cd = 0
cm = 0
cy = 0
#  Extracting Date
date_of_birth = dob[0:2]
date_of_current_date = current_date[0:2]

if date_of_birth == '01':
    dd = 1
elif date_of_birth == '02':
    dd = 2
elif date_of_birth == '03':
    dd = 3
elif date_of_birth == '04':
    dd = 4
elif date_of_birth == '05':
    dd = 5
elif date_of_birth == '06':
    dd = 6
elif date_of_birth == '07':
    dd = 7
elif date_of_birth == '08':
    dd = 8
elif date_of_birth == '09':
    dd = 9
else:
    dd = int(date_of_birth)

if date_of_current_date == '01':
    cd = 1
elif date_of_current_date == '02':
    cd = 2
elif date_of_current_date == '03':
    cd = 3
elif date_of_current_date == '04':
    cd = 4
elif date_of_current_date == '05':
    cd = 5
elif date_of_current_date == '06':
    cd = 6
elif date_of_current_date == '07':
    cd = 7
elif date_of_current_date == '08':
    cd = 8
elif date_of_current_date == '09':
    cd = 9
else:
    cd = int(date_of_current_date)


#  Extracting Month

month_of_birth = dob[3:6]
month_of_current_date = current_date[3:6]
month_of_birth = month_of_birth.capitalize()
month_of_current_date = month_of_current_date.capitalize()
if month_of_birth == 'Jan':
    mm = 1
elif month_of_birth == 'Feb':
    mm = 2
elif month_of_birth == 'Mar':
    mm = 3
elif month_of_birth == 'Apr':
    mm = 4
elif month_of_birth == 'May':
    mm = 5
elif month_of_birth == 'Jun':
    mm = 6
elif month_of_birth == 'Jul':
    mm = 7
elif month_of_birth == 'Aug':
    mm = 8
elif month_of_birth == 'Sep':
    mm = 9
elif month_of_birth == 'Oct':
    mm = 10
elif month_of_birth == 'Nov':
    mm = 11
elif month_of_birth == 'Dec':
    mm = 12


if month_of_current_date == 'Jan':
    cm = 1
elif month_of_current_date == 'Feb':
    cm = 2
elif month_of_current_date == 'Mar':
    cm = 3
elif month_of_current_date == 'Apr':
    cm = 4
elif month_of_current_date == 'May':
    cm = 5
elif month_of_current_date == 'Jun':
    cm = 6
elif month_of_current_date == 'Jul':
    cm = 7
elif month_of_current_date == 'Aug':
    cm = 8
elif month_of_current_date == 'Sep':
    cm = 9
elif month_of_current_date == 'Oct':
    cm = 10
elif month_of_current_date == 'Nov':
    cm = 11
elif month_of_current_date == 'Dec':
    cm = 12


#  Extracting Year
dob = dob[::-1]
x = dob[0:4]
x = x[::-1]
yy = int(x)



current_date = current_date[::-1]
xx = current_date[0:4]
xx = xx[::-1]
cy = int(xx)


born_date = date(yy, mm, dd)
current_date = date(cy, cm, cd)
number_of_days = current_date - born_date
print(f"\nYou have been alive for {number_of_days} days.")