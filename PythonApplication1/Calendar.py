print("=========== calendar =========== ")
import calendar

print(calendar.calendar(2020))  # same: calendar.prcal(2020)

print(calendar.prmonth(2020, 1))

calendar.weekday(2020, 1, 31)  # Mon: 0  .... Sun: 6

calendar.monthrange(2020,1)  # return what is weekday of first date of parameter and what is last day of parameter



