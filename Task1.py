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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

telephone_numbers = []

for text in texts:

    from_number, to_number, timestamp = text

    if from_number not in telephone_numbers:
        telephone_numbers.append(from_number)
    if to_number not in telephone_numbers:
        telephone_numbers.append(to_number)

for call in calls:

    from_number, to_number, timestamp, duration = call

    if from_number not in telephone_numbers:
        telephone_numbers.append(from_number)
    if to_number not in telephone_numbers:
        telephone_numbers.append(to_number)

print(len(telephone_numbers))
