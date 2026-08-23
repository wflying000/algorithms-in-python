"""
https://leetcode.cn/problems/rotate-array
"""


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:

        self.rotate_2(nums, k)
    
    def rotate_2(self, nums, k):
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left],  nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate_1(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]


    


def main():
    sln = Solution()
    nums = [0, 1, 2, 3, 4, 5, 6, 7]
    k = 3
    sln.rotate(nums, k)
    print(nums)

if __name__ == "__main__":
    main()