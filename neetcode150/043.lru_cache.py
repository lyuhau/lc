class ListNode:
    def __init__(self, key=None, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.val)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.ll_head = ListNode()
        self.ll_tail = ListNode()
        self.ll_head.next = self.ll_tail
        self.ll_tail.prev = self.ll_head

    def _update(self, node: ListNode) -> None:
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = self.ll_head
        node.next = self.ll_head.next
        self.ll_head.next.prev = node
        self.ll_head.next = node

    def _make_space(self):
        del self.map[self.ll_tail.prev.key]
        self.ll_tail.prev = self.ll_tail.prev.prev
        self.ll_tail.prev.next = self.ll_tail

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
        else:
            self.map[key] = node = ListNode(key, value)
            if len(self.map) > self.capacity:
                self._make_space()
        self._update(node)


if __name__ == '__main__':
    ["LRUCache", [2], "put", [1, 1], "put", [2, 2], "get", [1], "put", [3, 3], "get", [2], "put", [4, 4], "get", [1], "get", [3], "get", [4]]
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
