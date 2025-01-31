# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res=numBottles
        
        while numBottles>=numExchange:
            remain=numBottles%numExchange
            numBottles=numBottles//numExchange
            res+=numBottles
            numBottles+=remain
        return res