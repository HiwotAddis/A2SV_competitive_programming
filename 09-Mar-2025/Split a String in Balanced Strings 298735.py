# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l=0
        r=1
        count=0
        while r<=len(s):
            if s[l:r].count('L')==s[l:r].count('R'):
                count+=1
                l=r
            r+=1
        return count