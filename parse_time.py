import datetime

s = "[2010-01-01 18:48:14.631]"
print s
dt = datetime.datetime.strptime(s, "[%Y-%m-%d %H:%M:%S.%f]")
print dt.strftime("%H:%M:%S")
# datetime.datetime(2010, 1, 1, 18, 48, 14, 631829)
