from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = {}
        self.capacity = capacity
        self.qe = deque([])

    def __repr__(self):
        return f'LRU_Cache({self.cache})'

    def most_recently_used(self, key):
        if key in self.qe:
            self.qe.remove(key)
        self.qe.appendleft(key)

    def least_recently_used(self):
        try:
            return self.qe.pop()
        except IndexError:
            return None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.cache:
            return -1
        # set most recent
        self.most_recently_used(key)
        return self.cache[key]

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        self.most_recently_used(key) 
        if len(self.cache) >= self.capacity:
            lru = self.least_recently_used()
            del self.cache[lru]
            self.cache[key] = value
        else:
            self.cache[key] = value

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(5))
print(our_cache.get(6))

our_cache.set(7, 1234)
our_cache.set(8, 123)
our_cache.set(6, 101)  # least recently used not deleted
our_cache.set(3, 900)

print(our_cache.get(1))       # returns -1
print(our_cache.get(2))       # returns -1
print(our_cache.get(9))      # returns -1
print(our_cache)