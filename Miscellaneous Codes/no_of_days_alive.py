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
cccy = yy


current_date = current_date[::-1]
xx = current_date[0:4]
xx = xx[::-1]
cy = int(xx)
cy -= 1


days = 0

if mm == 1:
    days = 31
if mm == 2:
    if yy % 4 == 0:
        days = 29
    else:
        days = 28
if mm == 3:
    days = 31
if mm == 4:
    days = 30
if mm == 5:
    days = 31
if mm == 6:
    days = 30
if mm == 7:
    days = 31
if mm == 8:
    days = 31
if mm == 9:
    days = 30
if mm == 10:
    days = 31
if mm == 11:
    days = 30
if mm == 12:
    days = 31

tot_day = 0
day_left = days-dd


tot_day += day_left
if yy % 4 != 0:
    dob_year_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
                     6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
else:
    dob_year_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31,
                     6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
while(mm != 12):
    tot_day += dob_year_dict[mm]
    mm += 1


ccy = cy+1
if ccy % 4 != 0:
    c_year_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
                   6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
else:
    c_year_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31,
                   6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

while(yy != cy):
    if yy % 4 == 0:
        tot_day += 366
    else:
        tot_day += 365
    yy += 1

tot_day += cd
cm = cm-1
while(cm != 0):
    tot_day += c_year_dict[cm]
    cm -= 1

print(f"\nYou have been alive for {tot_day} days")