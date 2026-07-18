"""
https://leetcode.cn/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/description/?envType=study-plan-v2&envId=coding-interviews

有效数字（按顺序）可以分成以下几个部分：

若干空格
一个 小数 或者 整数
（可选）一个 'e' 或 'E' ，后面跟着一个 整数
若干空格
小数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
下述格式之一：
至少一位数字，后面跟着一个点 '.'
至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
一个点 '.' ，后面跟着至少一位数字
整数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
至少一位数字
部分有效数字列举如下：["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]

部分无效数字列举如下：["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。

 

示例 1：

输入：s = "0"
输出：true
示例 2：

输入：s = "e"
输出：false
示例 3：

输入：s = "."
输出：false
 

提示：

1 <= s.length <= 20
s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，空格 ' ' 或者点 '.' 。

"""

import re

class Solution:

    def validNumber(self, s: str) -> bool:

        # return self.valid_number_loop(s)

        return self.valid_number_regex(s)
    

    def valid_number_regex(self, s: str) -> bool:
        pattern = r"^\s*([+-])?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?\s*$"
        return bool(re.match(pattern, s))
        


    def valid_number_loop(self, s: str) -> bool:
        
        s = s.strip()
        is_e = False
        is_dot = False
        is_num = False
        for i in range(len(s)):
            ch = s[i]
            if ch == '+' or ch == '-':
                if i != 0 and (s[i - 1] != 'e' and s[i - 1] != 'E'):
                    return False
            elif ch == '.':
                if is_dot or is_e:
                    return False
                is_dot = True
            elif ch == 'e' or ch == 'E':
                if (not is_num) or is_e:
                    return False
                is_e = True
                is_num = False
            elif ch.isdigit():
                is_num = True
            else:
                return False
        
        return is_num

def main():
    sln = Solution()
    res = sln.validNumber("+1.2")
    print(res)


if __name__ == "__main__":
    main()