#Day 11 - How many seconds are in a year? 
#a year could be a leap year. 
secondsYear = (7*31*60*60*24) + 5*(30*60*60*24)
print(secondsYear)
#---------------------
days_this_year = int(input("How many days are in this year? >"))

normalYearDays =  365
leapYearDays = 366

hoursInDay = 24
hourMinutes = 60
minuteSeconds = 60

result_normal = normalYearDays * hoursInDay * hourMinutes * minuteSeconds

result_leap = leapYearDays * hoursInDay* hourMinutes * minuteSeconds

if days_this_year == 366:
  print("It's a leap year! There's ", result_leap, " seconds in this year!")
else:
  print("There's ", result_normal, " seconds this year")