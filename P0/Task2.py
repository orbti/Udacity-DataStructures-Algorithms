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
def parseAllCalls(calls):
    all_calls = []
    for call in calls:
        in_call = (call[1], int(call[3]))
        out_call = (call[0], int(call[3]))
        all_calls.append(in_call)
        all_calls.append(out_call)
    return all_calls

def longestPhoneCall(calls):
    all_calls = parseAllCalls(calls)
    d = {}
    for call in all_calls:
        number = call[0]
        time = call[1]
        if number not in d:
            d[number] = 0
        d[number] += time
    max_value = max(d, key=d.get)
    return (max_value, d[max_value])

if __name__ == '__main__':
    longest_call= longestPhoneCall(calls)
    print(f"{longest_call[0]} spent the longest time, {longest_call[1]} seconds, on the phone during September 2016.")
