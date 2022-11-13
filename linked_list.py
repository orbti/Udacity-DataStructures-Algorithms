class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def print_linked_list(self):
        node = self.head
        while node:
            print(f'[{node.value}]', end='')
            node = node.next

    def append(self, value):
        """Append a value to the end of the list."""
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        self.tail.next = Node(value)
        self.tail = self.tail.next
        return

    def prepend(self, value):
        """Prepend a value to the beginning of the list."""
        if self.head is None:
            self.head = Node(value)
            return
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def search(self, value):
        """Search the linked list for a node with the requested value and return the node."""
        if self.head is None:
            return

        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
            
        raise ValueError("Value not in linked list.")

    def remove(self, value):
        """Remove first occurrence of value."""
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next

        raise ValueError("Value not in linked list.")

    def pop(self):
        """Return the first node's value and remove it from the list."""
        if self.head is None:
            return

        pop_node = self.head
        self.head = self.head.next
        return pop_node.value

    def insert(self, value, pos):
        """Insert value at pos position in the list. 
        If pos is larger than the length of the list, 
        append to the end of the list."""
        # if the list is empty
        if self.head is None:
            self.head = Node(value)
            return

        if pos == 0:
            self.prepend(value)
            return

        index = 0
        node = self.head
        while node.next and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return

            node = node.next
            index += 1
        else:
            self.append(value)
            return

    def size(self):
        """Return the size or length of the linked list."""
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

if __name__ == '__main__':
    input_list = [1,2,3,4,5,6,7]
    linked_list = LinkedList()
    for v in input_list:
        linked_list.append(v)
    linked_list.print_linked_list()
