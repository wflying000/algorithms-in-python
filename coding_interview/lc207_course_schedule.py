"""
https://leetcode.cn/problems/course-schedule
"""
from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # return self.judge_dfs(numCourses, prerequisites)
        return self.judge_bfs(numCourses, prerequisites)

    def judge_dfs(self, numCourses, prerequisites):
        edges = defaultdict(list)
        visited = [0] * numCourses
        valid = True

        for pair in prerequisites:
            edges[pair[1]].append(pair[0])

        def dfs(u):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2
        
        for i in range(numCourses):
            if valid and visited[i] == 0:
                dfs(i)
        
        return valid
        
    def judge_bfs(self, numCourses, prerequisites):
        edges = defaultdict(list)
        indeg = [0] * numCourses

        for pair in prerequisites:
            edges[pair[1]].append(pair[0])
            indeg[pair[0]] += 1
        q = deque([u for u in range(numCourses) if indeg[u] == 0])

        count = 0
        while q:
            count += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        
        return count == numCourses



def main():
    sln = Solution()
    numCourses = 3
    prerequisites = [[0, 1], [0, 2], [2, 1]]
    res = sln.canFinish(numCourses, prerequisites)
    print(res)


if __name__ == "__main__":
    main()
