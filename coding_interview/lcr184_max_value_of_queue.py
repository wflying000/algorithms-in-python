"""
https://leetcode.cn/problems/dui-lie-de-zui-da-zhi-lcof/?envType=study-plan-v2&envId=coding-interviews
"""

from collections import deque

class MaxQueue:

    def __init__(self):
        self.data = deque()
        self.max_data = deque()
        

    def get_max(self) -> int:
        if not self.max_data:
            return -1
        return self.max_data[0]

    def add(self, value: int) -> None:
        self.data.append(value)
        while self.max_data and self.max_data[-1] < value:
            self.max_data.pop()
        self.max_data.append(value)

    def remove(self) -> int:
        if not self.data:
            return -1
        res = self.data.popleft()
        if res == self.max_data[0]:
            self.max_data.popleft()
        return res


def main():
    queue = MaxQueue()
    queue.add(1)
    print(queue.get_max())
    queue.add(2)
    queue.add(3)
    print(queue.get_max())
    queue.remove()
    print(queue.get_max())


if __name__ == "__main__":
    main()