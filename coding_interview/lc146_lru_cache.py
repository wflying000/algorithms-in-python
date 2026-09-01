"""
https://leetcode.cn/problems/lru-cache
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.list = LinkedList()
        self.key2node = {}
        self.node2key = {}
        
    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1
        node = self.key2node[key]
        self.list.move_to_first(node)
        return node.get_value()

    def put(self, key: int, value: int) -> None:

        if key in self.key2node:
            node = self.key2node[key]
            node.set_value(value)
            self.list.move_to_first(node)
        else:
            node = Node(value)
            self.key2node[key] = node
            self.node2key[node] = key
            if self.list.get_size() >= self.capacity:
                last = self.list.delete_last()
                old_key = self.node2key[last]
                self.node2key.pop(last)
                self.key2node.pop(old_key)
            self.list.add_first(node)


class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
    
    def get_value(self):
        return self.val

    def set_value(self, val):
        self.val = val
    
class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get_size(self):
        return self.size

    def move_to_first(self, node):
        if not node:
            return
        self.delete(node)
        self.add_first(node)
    
    def add_first(self, node):
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node
        self.size += 1
    
    def delete(self, node):
        if self.head.next == self.tail or not node:
            return
        
        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

    def delete_last(self):
        last = self.tail.prev
        self.delete(last)
        return last
        


def main():
    capacity = 2
    lru_cache = LRUCache(capacity)
    operations = ["put", "put", "get", "put", "get", "put", "get", "get", "get"]
    operators = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    expected_outputs = [None, None, 1, None, -1, None, -1, 3, 4]

    assert len(operations) == len(operators) == len(expected_outputs)

    for operation, operator, expected_output in zip(operations, operators, expected_outputs):
        if operation == "put":
            key, value = operator
            lru_cache.put(key, value)
        else:
            key = operator[0]
            actual_output = lru_cache.get(key)
            assert actual_output == expected_output


if __name__ == "__main__":
    main()
    