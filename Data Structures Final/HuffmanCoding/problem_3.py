import sys
import heapq

class Node:

    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.code = ''

    def __lt__(self, otherNode):
        return self.freq < otherNode.freq
    
    def __gt__(self, otherNode):
        return self.freq > otherNode.freq

    def __repr__(self):
        return f'Node({self.freq}, "{self.char}")'


def calculate_frequency(data):
    """Helper function to calculate frequency of each charecter."""
    chars = dict()
    for char in data:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


codes = dict()
def calculate_codes(node, val=''):
    """Helper function to calculate codes for each charecter."""
    newVal = val + str(node.code)
    if node.left:
        calculate_codes(node.left, newVal)
    if node.right:
        calculate_codes(node.right, newVal)
    if (node.left is None) and (node.right is None):
        codes[node.char] = newVal
    return codes


def huffman_output(codes: dict, data: str) -> str:
    """Helper function to convert char to coded string."""
    output = ''
    for char in data:
        output += codes[char]
    return output


def huffman_encoding(data: str) -> tuple:
    #Create frequency table
    chars_with_frequency = calculate_frequency(data)
    #print(chars_with_frequency)

    #Create an array of Nodes for priority queue.
    pq = []
    for char, freq in chars_with_frequency.items():
        pq.append(Node(freq, char))
    heapq.heapify(pq)

    while len(pq) > 1:
        #Select smallest nodes in priority queue
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)

        #Set node direction
        left.code = 0
        right.code = 1

        #Sum up left and right frequency and create new node
        newNode = Node(left.freq+right.freq, left.char+right.char, left, right)

        #Append newNode into priority queue
        heapq.heappush(pq, newNode)
    try:
        tree = heapq.heappop(pq)
        codes = calculate_codes(tree)
        #print(f'Charecters with Codes: {codes}')
        encoded_data = huffman_output(codes, data)
        #print(f'Encoded data: {encoded_data}')
        return encoded_data, tree
    except IndexError:
        print('No Node in tree.')
    

def huffman_decoding(data,tree):
    string = ''
    curNode = tree
    for bit in data:
        #Check if current node has a left or right node.
        if curNode.left is None and curNode.right is None:
            #Add char to string then reset back to root.
            string = string + curNode.char
            curNode = tree
            #Move down tree based on bit direction.
            if bit == '0':
                curNode = curNode.left
            if bit == '1':
                curNode = curNode.right
        else:
            #Move down tree based on bit direction.
            if bit == '0':
                curNode = curNode.left
            if bit == '1':
                curNode = curNode.right
    #Add last char.
    string = string + curNode.char
    return string

if __name__ == "__main__":
    codes = {}

    # a_great_sentence = "The bird is the word"
    a_great_sentence = 'The bird is the word'

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Add your own test cases: include at least three test cases
    # and two of them must include edge cases, such as null, empty or very large values

    # Test Case 1
    long_paragraph = "aaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    print ("The size of the data is: {}\n".format(sys.getsizeof(long_paragraph)))
    print ("The content of the data is: {}\n".format(long_paragraph))

    encoded_data, tree = huffman_encoding(long_paragraph)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    # Test Case 2
    long_paragraph = "a"

    print ("The size of the data is: {}\n".format(sys.getsizeof(long_paragraph)))
    print ("The content of the data is: {}\n".format(long_paragraph))

    encoded_data, tree = huffman_encoding(long_paragraph)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Test Case 3
    long_paragraph = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(long_paragraph)))
    print ("The content of the data is: {}\n".format(long_paragraph))

    encoded_data, tree = huffman_encoding(long_paragraph)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
