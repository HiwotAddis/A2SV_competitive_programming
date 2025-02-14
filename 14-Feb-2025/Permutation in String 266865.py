# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1=Counter(s1)
        l=0
        r=len(s1)
        while r<=len(s2):
            if count_s1==Counter(s2[l:r]):
                return True
            l+=1
            r+=1
        return False