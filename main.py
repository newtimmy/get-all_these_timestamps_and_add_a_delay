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
        #print(seconds)
        if len(list[len(list)-2]) == 1:
            list[1] = "0" + list[1]

        #print(minutes)
        #print("else")

    for element in list:
        return_list+= element
        return_list+= ":"

    return return_list

import datetime
import re

delay = 35

pattern = re.compile("[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]")

from datetime import timedelta

for line in range(100):
    with open('readme.txt',"a") as variable_name:
        variable_name.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now() + timedelta(seconds=line)) + "\n")

for i, line in enumerate(open('readme.txt')):
    for match in re.finditer(pattern, line):
        print('Found on line %s: %s' % (i+1, add_delay(match.group(), delay)))

        # Read in the file
        with open('readme.txt', 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(match.group(), add_delay(match.group(), delay))

        # Write the file out again
        with open('readme.txt', 'w') as file:
            file.write(filedata)
