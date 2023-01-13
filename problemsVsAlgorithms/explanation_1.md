P1 Sqaure Root of an Integer:
    The requriement of this algorithm is O(log n). I decided to use binary search to find the square root. Binary search has a time complecity of O(log n) and a space complexity of O(1).

P2 Search in a Rotated Sorted Array:
    The expecte time complexity is O(log n). I decided to binary search recursavily. I made sure that the number being searched is part of the array by checking if the left element is higher or equal to the number and if the mid element is greater than the search number. Once the mid element equals the search number we will return the index.

P3 Rearrange Array Digits:
    The expected time complexity is O(n log n). I decied to use quicksort to sort the array before      selecting the digits to be joined. The time complexity is O(n log n) and the space complexity is O(log n)

P4 Dutch National Flag:
    The expected time complexity is O(n). I decided to use a while loop to move through the array on both sides checking if the element is a 0 or 2 then placing it either on the left side of the array or right side array. The time complexity is O(n) and space complexity is O(n).

P5 Autocomplete with Tries:
    Suffixes time complexity is O(n*h) and space complexity is O(n). Insert time complexity is O(n) and space complexity is O(1). Find time complexity is O(h) and space complexity of O(1).

P6 Unsorted Integer Array:
The time complexity of get_min_max is O(n) with a space complexity of O(1)

P7 Request Routing in a Web Server with a Trie:
    Insert tiem complexity is O(n) and space complexity is O(1). Find time complexity is O(h) and space complexity is O(1). Add_handler is the same as insert with a time complexity of O(n) and space complexity of O(1). Lookup time complexity is O(n) because the split_path method is O(n) and the find method is O(n). The space complexity is O(n). Split_path time complexity is O(n) with a space complexity of O(n).
