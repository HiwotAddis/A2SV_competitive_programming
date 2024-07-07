class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0:
                return 1
            if n < 0:
                return 1 / pow(x, -n)
            if n % 2 == 0:
                return pow(x*x, n//2)
            else:
                return x * pow(x, n-1)
        return pow(x,n)
