"""
https://leetcode.cn/problems/implement-queue-using-stacks/description/


https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/?envType=study-plan-v2&envId=coding-interviews
"""

from collections import deque

class MyQueue:

    def __init__(self):
        self.data1 = deque()
        self.data2 = deque()
        

    def push(self, x: int) -> None:
        self.data1.append(x)

    def pop(self) -> int:
        self._move_data()
        if self.empty():
            return None
        return self.data2.pop()


    def peek(self) -> int:
        self._move_data()
        if self.empty():
            return None
        return self.data2[-1]

    def empty(self) -> bool:
        return (not self.data1) and (not self.data2)

    def _move_data(self):
        if not self.data2:
            while self.data1:
                self.data2.append(self.data1.pop())


def main():
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    print("peek  ->", q.peek())
    print("pop   ->", q.pop())
    print("pop   ->", q.pop())
    print("empty ->", q.empty())
    print("pop   ->", q.pop())
    print("empty ->", q.empty())

if __name__ == "__main__":
    main()
