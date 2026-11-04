class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.value
        
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)

        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

    def insert (self, node):
        prev = self.tail.prev 

        self.tail.prev.next = node
        node.prev = prev 

        node.next = self.tail
        self.tail.prev = node 

    def remove (self, node): 
        next_node = node.next
        prev_node = node.prev

        prev_node.next = next_node
        next_node.prev = prev_node
