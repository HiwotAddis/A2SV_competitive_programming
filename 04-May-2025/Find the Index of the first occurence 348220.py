# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h=len(haystack)
        n=len(needle)
        if n>h:
            return -1
        win=haystack[:n]
        if win==needle:
            return 0
        for i in range(n,h):
            win=win[1:]+haystack[i]
            if win==needle:
                return i-n+1
        return -1
        