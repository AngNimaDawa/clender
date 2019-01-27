import calander
help(calander.isleap)
year = 2014

while not calender.isleap(year):
    year += 1
print('the next laep year: ', year)
print(dir(calander))
print('the number of leap years between 2000 and 2050: ', calander.leapdays(2000,2051))
day = calander.weekday(2016,07,9)
if day == 0:
    day = 'monday'
elif day == 1:
    day = 'tuesday'
elif day == 2:
    day = 'wenesday'
elif day == 3:
    day = 'thursday'
elif day == 4:
    day = 'friday'
elif day == 5:
    day = 'saturday'
elif day == 6:
    day = 'sunday'

print('the day of the week for july 29, 2016 is', day)
