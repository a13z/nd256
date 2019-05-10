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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# PART A
import re

def bangalore_number(number):

    return number.startswith('(080)')

area_codes = set()
total_number_of_calls_from_bangalore = 0
total_number_of_calls_from_to_bangalore = 0

for call in calls:

    from_number, to_number, start_timestamp, duration = call

    if bangalore_number(from_number):
        # find area codes in the to_number, 2 cases: landlines or mobiles
        landline_prefix = re.compile(r"\((0\d+)\)")
        mobile_prefix = re.compile('(^[789]\d\d\d)')

        found_landline = landline_prefix.match(to_number)
        found_mobile = mobile_prefix.match(to_number)

        if found_landline:
            area_codes.add(found_landline.group(1))
        elif found_mobile:
            area_codes.add(found_mobile.group())

        if bangalore_number(to_number):
            total_number_of_calls_from_to_bangalore += 1

        total_number_of_calls_from_bangalore += 1

print("The numbers called by people in Bangalore have codes:")
for area_code in sorted(area_codes):
    print(area_code)


# PART B. Counters implemented in PART A as suggested by the reviewer in https://review.udacity.com/#!/reviews/1824367

print("%0.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore." % ((total_number_of_calls_from_to_bangalore/total_number_of_calls_from_bangalore) * 100))