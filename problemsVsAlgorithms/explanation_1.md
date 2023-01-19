P1 Sqaure Root of an Integer:
    The requriement of this algorithm is O(log n). I decided to use binary search to find the square root. Binary search has a time complecity of O(log n) and a space complexity of O(1).

P2 Search in a Rotated Sorted Array:
    The expected time complexity is O(log n). I decided to use binary search recursavily. I made sure that the number being searched is part of the array by checking if the left element is higher or equal to the number and if the mid element is greater than the search number. Once the mid element equals the search number we will return the index. The time complexity is O(log n) and space complexity is O(log n).

P3 Rearrange Array Digits:
    The expected time complexity is O(n log n). I decied to use quicksort to sort the array before      selecting the digits to be joined. The time complexity is O(n log n) and the space complexity is O(log n)

P4 Dutch National Flag:
    The expected time complexity is O(n). I decided to use a while loop to move through the array on both sides checking if the element is a 0 or 2 then placing it either on the left side of the array or right side array. The time complexity is O(n) and space complexity is O(1).

P5 Autocomplete with Tries:
    TrieNode().suffixes time complexity is O(n*h) and space complexity is O(n). In the TrieNode() I used the collections.defaultdict to help with adding children to the Trie.

    Trie().insert time complexity is O(n) and space complexity is O(1). 

    Trie().find time complexity is O(h) and space complexity of O(1).

P6 Unsorted Integer Array:
    The time complexity of get_min_max is O(n) with a space complexity of O(1)

P7 Request Routing in a Web Server with a Trie:
    RouteTrie().insert time complexity is O(n) and space complexity is O(1). 

    RouteTrie().find time complexity is O(h) and space complexity is O(1). 

    Router().add_handler time complexity of O(n) and space complexity of O(1). 

    Router().lookup time complexity is O(n). The space complexity is O(1). 

    Router().split_path time complexity is O(n) with a space complexity of O(1). I used the built in split function. This has a time complexity of O(n) because it has to look through the entire string to find each separatator.
