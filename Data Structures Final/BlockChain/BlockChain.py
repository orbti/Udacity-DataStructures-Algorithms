import hashlib
from datetime import datetime

def calc_hash(data: str):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Block:
    def __init__(self, timestamp, data, previous_hash=''):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.next = None
        self.previous = None

        #Claculate the blocks hash
        if self.previous_hash:
            hash_data = self.timestamp + self.data + self.previous_hash
            self.hash = calc_hash(hash_data)
        else:
            hash_data = self.timestamp + self.data
            self.hash = calc_hash(hash_data)

    def get_hash(self):
        return self.hash
    
    def __repr__(self):
        return f'Block(timestamp="{self.timestamp}", data="{self.data}", hash={self.hash}, previous_hash="{self.previous_hash}")'


class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None
        

    def add_block(self, data):
        timestamp = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        
        if self.head is None:
            self.head = Block(timestamp, data, None)
            self.tail = self.head
            return

        block = self.tail
        block.next = Block(timestamp, data, block.hash)
        block.next.previous = block
        self.tail = block.next
        return

    def print_chain(self):
        block = self.head
        print('START OF BLOCK CHAIN')
        print('----------------------------')
        while block:
            print(f'{block}')
            block = block.next
        print('----------------------------')
        print('END OF BLOCK CHAIN\n')
            

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
block_chain1 = BlockChain()
block_chain1.add_block('more data')
block_chain1.add_block('some data')
block_chain1.add_block('different data')
block_chain1.print_chain()
# Test Case 2
block_chain2 = BlockChain()
block_chain2.add_block('more data')
block_chain2.add_block('more data')
block_chain2.add_block('more data')
block_chain2.print_chain()
# Test Case 3

