#---------------------------#
from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity):
       # Initialize class variables
       self.cache_cap = capacity
       self.cache_val = dict()
       self.cache_order = deque()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if non existant.
        return self.cache_val.get(key, -1)

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if len(self.cache_order) >= self.cache_cap:
            del self.cache_val[self.cache_order.popleft()]
        self.cache_order.append(key)
        self.cache_val[key] = value

# Testing
def testing(x):
    x.set(1, 1);
    x.set(2, 2);
    x.set(3, 3);
    x.set(4, 4);


    print(x.get(1))
    print(x.get(2))
    print(x.get(9))

    x.set(5, 5) 
    x.set(6, 6)

    print(x.get(3))

for e in [5,1,3]:
    our_cache = LRU_Cache(e)
    testing(our_cache)

