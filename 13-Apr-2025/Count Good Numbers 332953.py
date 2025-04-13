# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        evens=(n+1)//2
        odds=n//2
        res=pow(5,evens,MOD)* pow(4,odds,MOD)
        return res%MOD