class LRUNode:
    def __init__(self, key = -1, val = -1, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __str__(self) -> None:
        walker = self.head.next
        sb = []
        while walker != self.tail:
            sb.append(f"(key: {walker.key}, val: {walker.val})")
            walker = walker.next
        return "-->".join(sb)

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = LRUNode()
        self.tail = LRUNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        valToReturn = self.cache[key].val
        self.update(key)
        return valToReturn

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.update(key)
        else:
            newNode = LRUNode(key, value, self.tail.prev, self.tail)
            self.tail.prev.next = self.tail.prev = newNode
            self.cache[key] = newNode
            if len(self.cache) > self.cap:
                keyToDelete = self.head.next.key
                self.evict()
                print(len(self.cache))
                del self.cache[keyToDelete]

    def update(self, key: int) -> None:
        target = self.cache[key]
        prev, next = target.prev, target.next
        prev.next, next.prev = next, prev
        mru = self.tail.prev
        mru.next = self.tail.prev = target
        target.prev, target.next = mru, self.tail

    def evict(self) -> None:
        lru = self.head.next
        next = lru.next
        self.head.next, next.prev = next, self.head
        lru.next = lru.prev = None

