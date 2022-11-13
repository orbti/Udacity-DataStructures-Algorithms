class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        self.tail.next = Node(value)
        self.tail = self.tail.next
        return

    def print_linked_list(self):
        node = self.head
        while node:
            print(f'[{node.value}]', end='')
            node = node.next

if __name__ == '__main__':
    input_list = [1,2,3,4,5,6,7]
    linked_list = LinkedList()
    for v in input_list:
        linked_list.append(v)
    linked_list.print_linked_list()