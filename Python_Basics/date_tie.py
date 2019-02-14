import datetime

mydate = datetime.datetime.now()
mymondaydate = mydate - datetime.timedelta(days=mydate.weekday())
mytuesdaydate = mymondaydate + datetime.timedelta(days=1)

print(mydate)
print(mymondaydate)
print(mytuesdaydate)