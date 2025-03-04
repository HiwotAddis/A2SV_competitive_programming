# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1])
        sum_=0
        for i in range(len(costs)//2):
            sum_+=costs[i][0]
        for i in range(len(costs)//2,len(costs)):
            sum_+=costs[i][1]
        return sum_