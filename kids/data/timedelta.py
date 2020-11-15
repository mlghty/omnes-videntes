import os
import psutil
import datetime
# top for print date and date 1

# bottom for getting current date


p = psutil.Process(3328)
p.create_time()

date = datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M")
date1 = datetime.datetime.fromtimestamp(p.create_time()).strftime("%H:%M")

print(date)
print(date1)
print("blank\n")

now = datetime.datetime.now()
print(now)
before = datetime.datetime.fromtimestamp(p.create_time())
print(before)
delta = now - before
print(delta)
