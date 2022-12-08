class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def search(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def append(self, value):

        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = Node(value)
        self.tail = self.tail.next

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

def union(llist_1, llist_2):
    # Your Solution Here
    llist = LinkedList()
    node1 = llist_1.head
    node2 = llist_2.head
    while node1:
        llist.append(node1.value)
        node1 = node1.next
    while node2:
        llist.append(node2.value)
        node2 = node2.next
    return llist

def intersection(llist_1, llist_2):
    # Your Solution Here
    cache = set()
    llist = LinkedList()
    node = llist_1.head
    while node:
        if node.value in cache:
            node = node.next
            continue
        if llist_2.search(node.value):
            llist.append(node.value)
            cache.add(node.value)
        node = node.next
    if llist.head is None:
        raise ValueError("No intersecting Node values in llist_1 and llist_2.")
    return llist

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3

