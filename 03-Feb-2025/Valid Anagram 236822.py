# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in set(s):
            for j in set(t):
                if s.count(i) ==t.count(i) and len(s)==len(t):
                    pass
                else:
                    return False
                
        return True