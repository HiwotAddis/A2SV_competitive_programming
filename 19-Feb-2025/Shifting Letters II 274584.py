# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        prefix=[0]*(n+1)
        for start,end,d in shifts:
            if d==1:
                prefix[start]+=1
                prefix[end+1]-=1
            else:
                prefix[start]-=1
                prefix[end+1]+=1
        
        current_shift = 0
        s = list(s)
        for i in range(n):
            current_shift += prefix[i]
            s[i] = chr((ord(s[i]) - ord('a') + current_shift) % 26 + ord('a'))
        
        return ''.join(s)
