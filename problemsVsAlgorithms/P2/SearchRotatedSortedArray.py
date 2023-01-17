"""Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array 
return its index, otherwise return -1.

You can assume there are no duplicates in the array and your 
algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Here is some boilerplate code and test cases to start with:
"""

def rotated_array_search(input_list, number):
    left = 0
    right = len(input_list)-1
    return rotated_array_search_recursion(input_list, number, left, right)

def rotated_array_search_recursion(input_list, number, left, right):
    if left > right:
        return -1
    
    mid = left + (right-left) // 2
    mid_element = input_list[mid]
    left_element = input_list[left]
    right_element = input_list[right]

    if mid_element == number:
        return mid
    
    if mid_element >= left_element:
        if left_element <= number and mid_element > number:
            return rotated_array_search_recursion(input_list, number, left, mid-1)
        else:
            return rotated_array_search_recursion(input_list, number, mid+1, right)
    else:
        if mid_element < number and right_element >= number:
            return rotated_array_search_recursion(input_list, number, mid+1, right)
        else:
            return rotated_array_search_recursion(input_list, number, left, mid-1)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 1, 2, 3, 4], 5])
test_function([[], 5])
test_function([[1], 5])
test_function([[1], 1])