"""
https://leetcode.cn/problems/3sum
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
 
        return res

            


            



def main():
    sln = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    nums = [-1, 0, 1, -1, 0, 1]
    res = sln.threeSum(nums)
    print(res)


if __name__ == "__main__":
    main()