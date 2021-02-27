import datetime
import math
import re
from playsound import playsound

x = input("Set Alarm Time (include am or pm) ")

floaters = re.findall("[+-]?\d+\.\d+", x)


time = floaters[0]
time = float(time)
time = math.modf(time)

minutes = time[0] * 100

hours = int(time[1])


minutes = round(minutes, 2)

#x_time = hour + minutes


# Extracting the am or pm
res = re.findall(r'\w+', x)

ampm = res[2]
ampm = ampm.lower()

if ampm == "pm":
    hours = hours + 12


print(datetime.datetime.now())
print(hours)
print(minutes)
file_input = input("Enter the filename: ")
while(True):

    if(hours == datetime.datetime.now().hour and minutes == datetime.datetime.now().minute):
        print("Wake up SleepyHead ")
        playsound(file_input)
        break

print("exited")
