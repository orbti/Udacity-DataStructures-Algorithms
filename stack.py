
"""Stack using an array.

This method has a time complexity problem. When
capacity is met we need to build a new array and
transfer all the elements to the new array.
"""
class Stack():
    def __init__(self, initial_size=10):
        self.arr = [None for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, data):
        if self.next_index == self.size():
            print("Out of space! Increasing array capacity...")
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None

        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def _handle_stack_capacity_full(self):
        old_arr = self.arr

        new_arr = [None for _ in range(2 * len(old_arr))]
        for index, element in enumerate(old_arr):
            new_arr[index] = element


"""
Stack using linked list.

Notice that if we pop or push an element with this stack, there's no traversal.
We simply add or remove the item from the head of the linked list, and update
the `head` reference. So with our linked list implementaion, `pop` and `push`
have a time complexity of O(1).

Also notice that using a linked list avoids the issue we ran into when we 
implemented our stack using an array. In that case, adding an item to the stack 
was fine—until we ran out of space. Then we would have to create an entirely new 
(larger) array and copy over all of the references from the old array.

That happened because, with an array, we had to specify some initial size (in other 
words, we had to set aside a contiguous block of memory in advance). But with a 
linked list, the nodes do not need to be contiguous. They can be scattered in 
different locations of memory, an that works just fine. This means that with a 
linked list, we can simply append as many nodes as we like. Using that as the 
underlying data structure for our stack means that we never run out of capacity, 
so pushing and popping items will always have a time complexity of O(1).
"""
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList():
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None

        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0
