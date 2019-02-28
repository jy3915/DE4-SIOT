import datetime
from weather_API import weather_API

date_time = datetime.datetime.now()
end_time = date_time + datetime.timedelta(days=1)
while True:
    if datetime.datetime.now() == end_time:
        weather_API()
        date_time = datetime.datetime.now()
        end_time = date_time + datetime.timedelta(days=1)


