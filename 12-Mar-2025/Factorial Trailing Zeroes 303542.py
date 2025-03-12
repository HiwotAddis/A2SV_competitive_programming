# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0:
            return 0
        Factorial=factorial(n)
        count=0
        while Factorial%10==0:
            count+=1
            Factorial//=10
        return count