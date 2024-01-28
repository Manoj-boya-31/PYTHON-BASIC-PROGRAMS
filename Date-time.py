# Date-time in python has a module called datetime to work with date and time properly.

# Return the year and name of weekday:
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

# To check month name by providing date in numbers:
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

# local date and time
import datetime
x = datetime.datetime.now()
print(x.strftime("%c"))