from datetime import datetime
import re

delay = 35

pattern = re.compile("[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}")

from datetime import timedelta
from random import randrange

print("Start creating:" + str(datetime.now()))

for line in range(100000):
    with open('readme.txt',"a") as variable_name:
        for i in range(randrange(4)):
            variable_name.write('Timestamp: {:%d.%m.%Y %H:%M:%S}'.format(datetime.now() + timedelta(seconds=line)) + "\n")

print("End creating:" + str(datetime.now()))

def add_delay(timestamp, delay):
    list = timestamp.split(":")

    return_list = ""

    if int(list[len(list) - 1]) + delay < 60:
        list[len(list) - 1] = str(round(int(list[len(list) - 1]) + delay))
    else:
        seconds = str(round((int(list[len(list) - 1]) + delay) % 60))
        minutes = str(round((int(list[len(list) - 1]) + delay) / 60) + round((int(list[len(list) - 2]))))
        list[len(list) - 2] = minutes
        list[len(list) - 1] = seconds

        if len(list[len(list)-1]) == 1:
            list[2] = "0" + list[2]

        if len(list[len(list)-2]) == 1:
            list[1] = "0" + list[1]

    for element in list:
        return_list+= element
        return_list+= ":"

    return return_list

print("Start:" + str(datetime.now()))
for i, line in enumerate(open('readme.txt')):
    for match in re.finditer(pattern, line):
        # Write the file out again
        with open('output.txt', 'a') as file:
            file.write(line.replace(match.group(), add_delay(match.group(), delay)))
    #if i == 3:
    #    break
print("End:" + str(datetime.now()))
