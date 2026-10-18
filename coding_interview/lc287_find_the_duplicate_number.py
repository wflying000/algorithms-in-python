"""
https://leetcode.cn/problems/find-the-duplicate-number/
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 把数组看成链表：下标 i 指向 nums[i]。
        # 因为数字都在 [1, n] 且存在重复，所以从 0 出发一定会进入环，
        # 环的入口就是那个重复的数字（有两条边指向它）。
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # 快慢指针相遇后，一个指针回到起点，再同速前进，
        # 再次相遇的位置就是环的入口。
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


def main():
    sln = Solution()

    nums = [1, 3, 4, 2, 2]
    print(sln.findDuplicate(nums))

    nums = [3, 1, 3, 4, 2]
    print(sln.findDuplicate(nums))

    nums = [1, 1]
    print(sln.findDuplicate(nums))

    nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
    print(sln.findDuplicate(nums))


if __name__ == "__main__":
    main()
