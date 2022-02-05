
from datetime import timedelta, tzinfo
import datetime
import pytz
d = datetime.date(2016, 7, 24)
#print(datetime.date(2016, 7, 24))
#print(d)
today=datetime.date.today()
#print(today)
#print(today.month)
#print(today.year)
#print(today.day)
#print(today.weekday())
#print(today.isoweekday())
tdelta = datetime.timedelta(days=7)
#print(today + tdelta)
bday = datetime.date(2017, 6, 20)
till_day = bday - today
#print(till_day)
#print(till_day.total_seconds())
t = datetime.datetime(2017, 11, 10, 9, 24, 23)
tdelta = datetime.timedelta(days=7)
#print(t)
#print(t + tdelta)
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

#print(dt_today)
#print(dt_now)
#print(dt_utcnow)
dt = datetime.datetime(2017, 11, 10, 9, 36, 55,tzinfo=pytz.UTC)
#print(dt)
dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
today = datetime.datetime.now()
#print(dt_mtn)
#print(dt_mtn.isoformat())
# print('today = ', today)
# #print(today.isoformat())
# print(datetime.MINYEAR)
# print(datetime.MAXYEAR)
# print(type(datetime.date))
# print(type(datetime))
# print(type(pytz))
# print(dir(datetime))
# help(datetime.date)
Hoan = datetime.datetime(1991, 6, 20)
today = datetime.datetime.now()
dt = datetime.timedelta(30)
#print(today)
#print(dt + today)
# Day-name, Month-name Day-#, Year
today_format = today.strftime("%A, %B %d, %Y")
Hoan_birthday = "Huynh Van Hoan was born on {:%A, %B %d, %Y}."
print(Hoan_birthday.format(Hoan))
print(type(tzinfo))

# It's so hard to understand these below line! need to see many times!
from datetime import timedelta, datetime, tzinfo
class GMT1(tzinfo):
	def utcoffset(self, dt):
		return timedelta(hours=1) + self.dst(dt)
	def dst(self, dt):
		d = datetime(dt.year, 4, 1)
		self.dston = d - timedelta(days=d.weekday() + 1)
		d = datetime(dt.year, 11, 1)
		self.dstoff = d - timedelta(days=d.weekday() + 1)
		if  self.dston <= dt.replace(tzinfo=None) < self.dstoff:
			return timedelta(hours=1)
		else: 
			return timedelta(0)
	def tzname(self, dt):
		return "GMT + 1"
gmt1 = GMT1()
dt1 = datetime(2006, 11, 21, 16, 30, tzinfo=gmt1)
dt1.dst()
dt1.utcoffset()
print(dt1.dst())
print(dt1.utcoffset())
help(tzinfo)