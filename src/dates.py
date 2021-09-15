import datetime
import pytz
#naive dates : easiest
d = datetime.date(2021,9,11) # not 09 leading zero will make error
print(d)
today = datetime.date.today()
print(today)
print(f'Year:{today.year}\nMonth:{today.month}\nDate:{today.day}')
print(today.weekday())
print(today.isoweekday())

tdelta = datetime.timedelta(days = 7)#timedelta
print(today - tdelta)
#aware dates enough information


t = datetime.time(9,29,39,400)
t.hour
dt = datetime.datetime(1996,3,15,14,20,00,3400)
print(dt.date())
print(dt.time())

tdelta = datetime.timedelta(days = 7)
print(dt + tdelta)


# different methods
dt_today = datetime.datetime.today() #timezone none
dt_now = datetime.datetime.now() #timezone option available
dt_utcnow = datetime.datetime.utcnow() #current utuc now
print(dt_today)
print(dt_now)
print(dt_utcnow)

dt_utcnow = datetime.datetime(2016,7,17,12,30,45,tzinfo = pytz.UTC)
print(f'UTC Now:{dt}')

dt_japan = dt_utcnow.astimezone(pytz.timezone('JAPAN'))
print(dt_japan)

# for tz in pytz.all_timezones:
#     print(tz)



dt_japan = datetime.datetime.now()
dt_east = dt_japan.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)


print(dt_japan.isoformat())
print(dt_japan.strftime('%B %d, %Y')) # converts to string

string_date = 'September 11, 2021'
print(datetime.datetime.strptime(string_date, '%B %d, %Y')) # converts to time