class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(input_list):
    head = None
    tail = None
    
    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next
    return head

def print_linked_list(head):
    current_node = head
    while current_node is not None:
        print(f'[{current_node.value}]', end='')
        current_node = current_node.next

if __name__ == '__main__':
    input_list = [1,2,3,4,5,6,7]
    head = create_linked_list(input_list)
    print_linked_list(head)