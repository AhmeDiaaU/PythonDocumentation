import datetime

dt = datetime.time(14,7)
print(dt)
print(datetime.time(14,7,59,300))
dt = datetime.date.today()
print(dt , type(dt))
print(dt.ctime()) # Sun Jan 26 00:00:00 2025
newdt = dt.replace(year= 1900 , day=1, month= 3) # to replace date in the original date 
delta = dt - newdt # calculate difference between two dates 
print(delta , type(delta))
dt = datetime.datetime(2022 , 1, 11, 14,7,59,300)
print(dt.ctime())