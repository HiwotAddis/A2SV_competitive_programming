# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        repet=0
        l=0
        res=float('-inf')
        if len(s)==1:
            return 1
        for r in range(1,len(s)):
            if s[r]==s[r-1]:
                repet+=1
            while repet>1:
                if s[l] ==s[l+1]:
                    repet-=1
                l+=1
            res=max(res,r-l+1)

        return res
# 