"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

phonedict = {}

for call in calls:

    telephone_number, receiving_number, start_timestamp, duration = call

    if telephone_number not in phonedict:
        phonedict[telephone_number] = int(duration)
    else:
        phonedict[telephone_number] += int(duration)

    if receiving_number not in phonedict:
        phonedict[receiving_number] = int(duration)
    else:
        phonedict[receiving_number] += int(duration)

telephone_number_longest_time = max(phonedict, key=lambda i: phonedict[i])

print("%r spent the longest time, %r seconds, on the phone during September 2016" % (telephone_number_longest_time, phonedict[telephone_number_longest_time]))