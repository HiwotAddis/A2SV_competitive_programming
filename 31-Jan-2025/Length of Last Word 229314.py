# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        s=s.split()
        return len(s[-1])