# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        Sum=0
        buy=0
        costs.sort()
        for i in range(len(costs)):
            Sum+=costs[i]
            if Sum<=coins:
                buy+=1
            else:
                break
        return buy
            