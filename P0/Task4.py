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

def noneTelemarketers(texts, calls):
    noneTelemarketers = {text[0] for text in texts}
    noneTelemarketers.update({text[1] for text in texts})
    noneTelemarketers.update({call[1] for call in calls})
    return noneTelemarketers

def isTelemarketer(texts, calls):
    none_telemarketers = noneTelemarketers(texts, calls)
    is_telemarketer = set()
    for call in calls:
        if call[0] in none_telemarketers:
            continue
        is_telemarketer.add(call[0])
    return is_telemarketer

if __name__ == '__main__':
    print("These numbers could be telemarketers: ")
    for i in sorted(isTelemarketer(texts, calls)):
        print(i)