"""Rearrange Array Elements
Rearrange Array Elements so as to form two number such that 
their sum is maximum. Return these two numbers. You can assume 
that all array elements are in the range [0, 9]. The number of 
digits in both the numbers cannot differ by more than 1. You're 
not allowed to use any sorting function that Python provides and 
the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected 
answer can be [542, 31]. In scenarios such as these when 
there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:
"""

def sort_a_little_bit(input_list, begin_index, end_index):
    left_index = begin_index
    pivot_index = end_index
    pivot_value = input_list[pivot_index]

    while pivot_index != left_index:
        num = input_list[left_index]

        if num <= pivot_value:
            left_index += 1
            continue

        input_list[left_index] = input_list[pivot_index-1]
        input_list[pivot_index-1] = pivot_value
        input_list[pivot_index] = num
        pivot_index -= 1
    return pivot_index

def sort_all(input_list, begin_index, end_index):
    if end_index <= begin_index:
        return
    
    pivot_index = sort_a_little_bit(input_list, begin_index, end_index)
    sort_all(input_list, begin_index, pivot_index-1)
    sort_all(input_list, pivot_index+1, end_index)
    

def quicksort(input_list):
    sort_all(input_list, 0, len(input_list)-1)
    return input_list

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number 
    such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not input_list:
        return []

    sorted_list = quicksort(input_list)
    
    num1_list = sorted_list[::-2]
    num2_list = sorted_list[len(sorted_list)-2::-2]

    num1 = int(''.join(map(str, num1_list)))
    num2 = int(''.join(map(str, num2_list)))

    return [num1, num2]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[],[]])