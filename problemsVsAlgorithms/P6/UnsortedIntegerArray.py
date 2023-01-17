"""Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer 
from a list of unsorted integers. The code should run in O(n) 
time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single 
traversal?
"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return 'No ints'

    min = ints[0]
    max = ints[0]

    for i in range(0, len(ints)-1):
        if ints[i] < min:
            min = ints[i]
        elif ints[i] > max:
            max = ints[i]
        
    return (min, max)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l2 = []
print ("Pass" if ('No ints' == get_min_max(l2)) else "Fail")

l3 = [i for i in range(0, 1320)]
random.shuffle(l3)
print("Pass" if ((0, 1319) == get_min_max(l3)) else "Fail")