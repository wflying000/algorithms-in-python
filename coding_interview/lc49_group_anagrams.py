"""
https://leetcode.cn/problems/group-anagrams/description/

"""

from typing import List

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        return self.process_count(strs)

    def process_count(self, strs):
        maps = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            if key not in maps:
                maps[key] = []
            maps[key].append(s)
        
        res = [v for k, v in maps.items()]
        return res
    

    def process_sort(self, strs):
        maps = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in maps:
                maps[key] = []
            maps[key].append(s)
        
        res = [v for k, v in maps.items()]
        return res
    
    

def main():
    sln = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = sln.groupAnagrams(strs)
    print(res)


if __name__ == "__main__":
    main()