## 💻 Exercises: Day 16

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
now = datetime.now()
day = now.day
month = now.month
year= now.year
hour = now.hour
minute= now.minute
timestamp = now.timestamp()

print(day, month, year, hour, minute)
print("Timestamp: " , timestamp)

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
from datetime import datetime

now = datetime.now()
t = now.strftime("%H:%M:%S")
print(t)
time_one = now.strftime("%m:%d:%Y ,%H:%M:%S" )
print(time_one)
# 3. Today is 5 December, 2019. Change this time string to time.
s = "5 December, 2019"
today = datetime.strptime(s, "%d %B, %Y")
print(today)
# 4. Calculate the time difference between now and new year.
# from datetime import date , datetime

# today = date(year=2026, month=8, day=1)
# new_year = date(year=2027, month=1, day=1)

# time_left = new_year - today

# print("Time left: " , time_left)

from datetime import date

today = date.today()
new_year = date(today.year + 1, 1, 1)

time_left = new_year - today

print("Time left:", time_left)

# 5. Calculate the time difference between 1 January 1970 and now.
# then = date(year=1970, month=1, day=1)

# diff = today - then

# print("Difference: ", diff)

from datetime import date

today = date.today()
then = date(1970, 1, 1)

diff = today - then

print("Difference:", diff)
# 6. Think, what can you use the datetime module for? Examples:

#    - Time series analysis
#    - To get a timestamp of any activities in an application
#    - Adding posts on a blog 

# 🎉 CONGRATULATIONS ! 🎉