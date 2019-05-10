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

numbers_making_calls = set([line[0] for line in calls])
numbers_receiving_calls_or_texting = set([line[1] for line in calls])

for text in texts:
    from_number, to_number, start_timestamp = text
    numbers_receiving_calls_or_texting.add(from_number)
    numbers_receiving_calls_or_texting.add(to_number)

possible_telemarketers = numbers_making_calls - numbers_receiving_calls_or_texting

print("These numbers could be telemarketers: ")
for possible_telemarketer in sorted(possible_telemarketers):
    print(possible_telemarketer)