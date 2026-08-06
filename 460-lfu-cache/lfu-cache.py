class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None 
        self.prev = None 
        self.count = 1

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def empty(self):
        return self.head.next == self.tail

    def append(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        self.tail.prev = node
        node.prev = prev_node
        node.next = self.tail

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        node.next = None
        node.prev = None

    def pop_left(self):
        if self.empty():
            return None
        node_to_remove = self.head.next
        self.remove(node_to_remove)
        return node_to_remove

class LFUCache:

    def __init__(self, capacity: int):
        self._cap = capacity
        self._node_map = {}
        self._level_to_ll = {}
        self._lowest_level = 0
        self._size = 0
        

    def get(self, key: int) -> int:
        if key not in self._node_map:
            return -1
        node = self._node_map[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self._cap == 0:
            return
        if key in self._node_map:
            node = self._node_map[key]
            node.val = value
            self._update(node)
            return node.val
        if self._cap == self._size:
            lfu = self._level_to_ll[self._lowest_level]
            node = lfu.pop_left()
            del self._node_map[node.key]
            self._size -= 1
            if lfu.empty():
                del self._level_to_ll[self._lowest_level]
        new_node = ListNode(key, value)
        self._node_map[key] = new_node
        if 1 not in self._level_to_ll:
            self._level_to_ll[1] = LinkedList()
        linked = self._level_to_ll[1]
        linked.append(new_node)
        self._lowest_level = 1
        self._size += 1

    def _update(self, node):
        old_freq = node.count
        linked = self._level_to_ll[old_freq]
        linked.remove(node)
        if linked.empty():
            del self._level_to_ll[old_freq]
            if old_freq == self._lowest_level:
                self._lowest_level += 1
        node.count += 1
        if node.count not in self._level_to_ll:
            self._level_to_ll[node.count] = LinkedList()
        new_linked = self._level_to_ll[node.count]
        new_linked.append(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)