import datetime

#now = datetime.datetime.now().isocalendar()[1]
year, week, dow = datetime.datetime.today().isocalendar()
week_start = datetime.datetime.strptime(str(year) + "-" + str(week-1) + "-0", "%Y-%W-%w")
result = [(week_start + datetime.timedelta(days=x)).day for x in range(1,13)]
print(result)
print(len(result))
print(year)
print(week_start)
week_start