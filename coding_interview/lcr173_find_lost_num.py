"""
https://leetcode.cn/problems/que-shi-de-shu-zi-lcof/description/?envType=study-plan-v2&envId=coding-interviews
"""


class Solution:
    def takeAttendance(self, records):
        res = self.search_binary(records)
        return res

    def search(self, records):
        for i in range(len(records)):
            if records[i] != i:
                return i
        
        return len(records)

    def search_binary(self, records):
        i, j = 0, len(records) - 1
        res = len(records)
        while i <= j:
            mid = (i + j) // 2
            if records[mid] == mid:
                i = mid + 1
            else:
                res = mid
                j = mid - 1
        
        return res



def main():
    nums = [0, 1, 2, 3, 5]
    sln = Solution()
    res = sln.takeAttendance(nums)
    print(res)



if __name__ == "__main__":
    main()