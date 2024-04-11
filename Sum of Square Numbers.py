class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(c**0.5)+1):
            b_sqr=c-a**2
            if (int(b_sqr**0.5))**2 ==b_sqr:
                return True
        return False
