"""
https://leetcode.cn/problems/decode-string
"""

from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        self.index = 0
        stack = deque()

        while self.index < len(s):
            ch = s[self.index]
            if ch.isdigit():
                number = self.get_number(s)
                stack.append(number)
            elif ch.isalpha() or ch == '[':
                stack.append(ch)
                self.index += 1
            else:
                str_list = []
                while stack:
                    if stack[-1] != '[':
                        str_list.append(stack.pop())
                    else:
                        stack.pop()
                        break
                number = int(stack.pop())
                strs = ("".join(reversed(str_list))) * number
                stack.append(strs)
                self.index += 1
        
        res = "".join([s for s in stack])
        return res
                
            

    def get_number(self, s):
        digits = []
        while self.index < len(s):
            ch = s[self.index]
            if ch.isdigit():
                digits.append(ch)
                self.index += 1
            else:
                break
        return "".join(digits)


def main():
    sln = Solution()
    s = "3[a]2[bc]"
    res = sln.decodeString(s)
    print(res)


if __name__ == "__main__":
    main()