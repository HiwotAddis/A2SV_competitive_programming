class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        t=0
        curr=1
        dxn=1
        while t<time:
            if 0<curr+dxn<=n:
                curr+=dxn
                t+=1
            else:
                dxn*=-1
        return curr
