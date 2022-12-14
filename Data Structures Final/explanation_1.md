Problem_1:
In problem_1 the data structure of choice was a queue. I used a queue to take advantage of its first in first out feature to keep track of the leaset used key. I also used a dictionary for the cache for easy key value look ups.
most_recently_used() --> O(1) time complexity and O(1) space complexity.
least_recently_used() --> O(1) time complexity and O(1) space complexity.
get() --> O(1) time complexity and O(1) space complexity.
set() --> O(1) time complexity and O(1) space complexity.

Problem_2:
In problem_2 I used a recursive stack to look through each folder and go deeper if there are more folders to return all files with a specific suffix.
find_files() --> O(k * n) time complexity and O(n) space complexity.

Problem_3:
I created three helper funcitons calculate_frequency(), calculate_codes() and huffman_output(). These three functions use a dictionary for easy key value pair look ups. The huffman_encoding() function uses a priority queue with a min-heap data structure to keep track of all the Nodes in sorted order to create a binary search tree. In huffman_decoding() we utilize the binary search tree and the encoded string created by huffman_encoding(). We traverse the tree using the encoded string checking if we get to a leaf node.
calculate_frequency() --> O(1) time complexity and O(n) space complexity.
calculate_codes() --> O(|v|) time complexity and O(h) space complexity.
huffman_output() --> O(n) time complexity and O(n) space complexity.
huffman_encoding() --> O(n log n) time complexity and O(n) space complexity.
huffman_decoding() --> O(n) time complexity and O(n) space complexity.

Problem_4:
In this problem i used a recursive stack to look through the groups to find if a user is in the group.
is_user_in_group() --> O(n) time complexity and O(nm) space complexity.

Problem_5:
I used a doubly linkedlist to create the BlockChain. Using a doubly linkedlist allows me to keep track of the connection to each Block in the BlockChain going in both directions.
Block.get_hash() --> O(1) time complexity and O(1) space complexity.
BlockChain.add_block() --> O(1) time complexity and O(n) space complexity.
BlockChain.print_chain() --> O(n) time complexity and O(1) space complexity.
BlockChain.check_chain() -- O(n) time complexity and O(1) space complexity.

Problem_6:
In this problem I used a LinkedList to create new linkedlist to uion or find the intersections. In the intersection fuction I used a set to keep track of the values I have visited.
union() --> O(k + n) time complexity and O(mn) space complexity.
intersection() -- > O(n) time complexity and O(mn) space complexity.