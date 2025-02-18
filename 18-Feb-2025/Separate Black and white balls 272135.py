# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        s=list(s)
        l=0
        count=0
        for r in range(0,len(s)):
            if s[r]=='0':
                s[r],s[l]=s[l],s[r]
                count+=r-l
                l+=1
        return count