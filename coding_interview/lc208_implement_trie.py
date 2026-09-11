"""
https://leetcode.cn/problems/implement-trie-prefix-tree
"""

class Node:
    def __init__(self, end=False):
        self.children = [False for _ in range(26)]
        self.end = end

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        base = ord('a')
        for i, c in enumerate(word):
            idx = ord(c) - base
            if not node.children[idx]:
                node.children[idx] = Node()
            node = node.children[idx]
            if i == len(word) - 1:
                node.end = True

    def search(self, word: str) -> bool:
        if not word:
            return False
        node = self.root
        base = ord('a')
        for c in word:
            idx = ord(c) - base
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.end
        

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return False
        node = self.root
        base = ord('a')
        for c in prefix:
            idx = ord(c) - base
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True
        

def main():

    trie = Trie()

    operations = ["insert", "search", "search", "startsWith", "insert", "search"]
    operators = [["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    expected_outputs = [None, True, False, True, None, True]

    assert len(operations) == len(operators) == len(expected_outputs)

    for operation, operator, expected_output in zip(operations, operators, expected_outputs):
        if operation == "insert":
            trie.insert(operator[0])
        elif operation == "search":
            actual_output = trie.search(operator[0])
            assert actual_output == expected_output
        elif operation == "startsWith":
            actual_output = trie.startsWith(operator[0])
            assert actual_output == expected_output


if __name__ == "__main__":
    main()

