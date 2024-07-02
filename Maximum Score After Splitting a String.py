class Solution:
    def maxScore(self, s: str) -> int:
        left=[]
        score=0
        right=list(s)
        while len(right)!=1:
            x=right.pop(0)
            left.append(x)
            Sum=left.count('0')+right.count('1')
            score=max(score,Sum)
        return score
