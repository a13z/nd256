"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

possible_telemarketers = list(dict.fromkeys([line[0] for line in calls]))

for number in possible_telemarketers:
    for call in calls:
        from_number, to_number, start_timestamp, duration = call
        if number == to_number:
            possible_telemarketers.remove(number)
            break

for number in possible_telemarketers:
    for text in texts:
        from_number, to_number, start_timestamp = text
        if number == to_number or number == from_number:
            possible_telemarketers.remove(number)
            break

print("These numbers could be telemarketers: ")
for possible_telemarketer in sorted(possible_telemarketers):
    print(possible_telemarketer)





