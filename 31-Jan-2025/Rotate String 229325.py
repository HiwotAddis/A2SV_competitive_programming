# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s==goal:
            return True
        for i in range(1,len(s)):
            temp=s[i:]+s[:i]
            print(s)
            if temp ==goal:
                return True
        return False