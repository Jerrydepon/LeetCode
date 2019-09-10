# method 1: double linked list + dictionary
#   dic: key-key, value-Node(key, value)
#   
# method 2: use OrderedDict()
#   the collections.OrderedDict() build a dictionary which appends new added pair in the end
#   use popitem(last=False) to pop oldest pair
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

# double linked list + dictionary
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            least = self.head.next
            self._remove(least)
            del self.dic[least.key]
    
    def _add(self, node):
        p = self.tail.prev
        p.next= node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node
    
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)




# # OrderedDict()
# import collections
# class LRUCache:
#     def __init__(self, Capacity):
#         self.capacity = Capacity
#         self.dic = collections.OrderedDict()

#     def get(self, key):
#         if key not in self.dic:
#             return -1
#         val = self.dic[key]
#         del self.dic[key]
#         self.dic[key] = val
#         return val

#     def put(self, key, val):
#         if key in self.dic:
#             del self.dic[key]
#         self.dic[key] = val
#         if len(self.dic) > self.capacity:
#             self.dic.popitem(last=False)