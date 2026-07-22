"""
https://leetcode.cn/problems/min-stack/description/

https://leetcode.cn/problems/bao-han-minhan-shu-de-zhan-lcof/?envType=study-plan-v2&envId=coding-interviews
"""

from collections import deque


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = deque()
        self.min_data = deque()

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.min_data:
            self.min_data.append(x)
        else:
            val = x if x < self.min_data[-1] else self.min_data[-1]
            self.min_data.append(val)

    def pop(self) -> None:
        self.data.pop()
        self.min_data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_data[-1]


def main():
    stack = MinStack()
    stack.push(1)
    print(stack.getMin())
    stack.push(2)
    stack.push(-1)
    print(stack.getMin())


if __name__ == "__main__":
    main()