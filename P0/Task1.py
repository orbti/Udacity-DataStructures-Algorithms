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
def countTelephoneNumbers(*args):
    numbers = set()
    for arg in args:
        for entry in arg:
            numbers.add(entry[0])
            numbers.add(entry[1])
    return len(numbers)

if __name__ == '__main__':
    print(f'There are {countTelephoneNumbers(calls, texts)} different telephone numbers in the records.')
