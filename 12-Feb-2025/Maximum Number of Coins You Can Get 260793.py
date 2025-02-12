# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True) 
        res=0
        iteration=len(piles)//3
        i=0
        for _ in range(iteration):
            res+=piles[i+1]
            i+=2
        return res