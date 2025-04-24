# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree=defaultdict(int)
        outdegree=defaultdict(int)
        for a,b in trust:
            indegree[b]+=1
            outdegree[a]+=1
        for i in range(1,n+1):
            if indegree[i]==n-1 and outdegree[i]==0:
                return i
        # print(indegree,outdegree)
        return -1

