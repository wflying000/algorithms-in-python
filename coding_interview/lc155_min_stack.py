"""
https://leetcode.cn/problems/min-stack
"""

from collections import deque


class MinStack:

    def __init__(self):
        self.data = deque()
        self.min_data = deque()

    def push(self, value: int) -> None:
        self.data.append(value)
        if (not self.min_data) or (value <= self.min_data[-1]):
            self.min_data.append(value) 

    def pop(self) -> None:
        value = self.data.pop()
        if value == self.min_data[-1]:
            self.min_data.pop()
        

    def top(self) -> int:
        
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_data[-1]
        


def main():
    min_stack = MinStack()
    min_stack.push(1)
    min_stack.push(2)
    print(f"min value: {min_stack.getMin()}")
    min_stack.push(0)
    print(f"min value: {min_stack.getMin()}")
    min_stack.pop()
    print(f"min value: {min_stack.getMin()}")


if __name__ == "__main__":
    main()