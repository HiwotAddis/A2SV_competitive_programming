# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        dict1={}
        dict2={}
        for i in range(len(s)):
            if (s[i] in dict1 and dict1[s[i]]!=t[i]) or (t[i] in dict2 and s[i]!=dict2[t[i]]):
                return False
            dict1[s[i]]=t[i]
            dict2[t[i]]=s[i]
        return True