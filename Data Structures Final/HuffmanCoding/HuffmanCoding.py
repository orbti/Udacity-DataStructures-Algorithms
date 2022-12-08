import sys

class Node:

    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.code = ''

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
        output = output + codes[char]
    return output


def huffman_encoding(data: str) -> tuple:
    #Create frequency table
    chars_with_frequency = calculate_frequency(data)
    # print(chars_with_frequency)

    #Create an array of Nodes for priority queue.
    pq = []
    for char, freq in chars_with_frequency.items():
        pq.append(Node(freq, char))
    while len(pq) > 1:
        #Sort nodes in priority queue based on their frequency
        pq = sorted(pq, key=lambda x: x.freq)

        #Select smallest nodes in priority queue
        left = pq.pop(0)
        right = pq.pop(0)

        #Set node direction
        left.code = 0
        right.code = 1

        #Sum up left and right frequency and create new node
        newNode = Node(left.freq+right.freq, left.char+right.char, left, right)

        #Append newNode into priority queue
        pq.append(newNode)

    tree = pq[0]
    codes = calculate_codes(tree)
    # print(f'Charecters with Codes: {codes}')
    encoded_data = huffman_output(codes, data)
    # print(f'Encoded data: {encoded_data}')
    return encoded_data, tree
    

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
    long_paragraph = """
    In general, a data compression algorithm reduces the amount of memory (bits) required to represent a 
    message (data). The compressed data, in turn, helps to reduce the transmission time from a sender to 
    receiver. The sender encodes the data, and the receiver decodes the encoded data. As part of this problem, 
    you have to implement the logic for both encoding and decoding. 
    A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, 
    there is a loss (lossy) or no loss (lossless) of information. The Huffman Coding is a lossless data 
    compression algorithm. Let us understand the two phases - encoding and decoding with the help of an example.
    A  . Huffman Encoding
    Assume that we have a string message AAAAAAABBBCCCCCCCDDEEEEEE comprising of 25 characters to be encoded. 
    The string message can be an unsorted one as well. We will have two phases in encoding - building the Huffman 
    tree (a binary tree), and generating the encoded data. The following steps illustrate the Huffman encoding:
    """

    print ("The size of the data is: {}\n".format(sys.getsizeof(long_paragraph)))
    print ("The content of the data is: {}\n".format(long_paragraph))

    encoded_data, tree = huffman_encoding(long_paragraph)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # Test Case 2
    
    # Test Case 3