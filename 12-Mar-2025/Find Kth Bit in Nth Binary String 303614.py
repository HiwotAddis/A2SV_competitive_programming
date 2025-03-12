# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        def invert(s):
            s=list(s)
            for i in range(len(s)):
                if s[i]=='0':
                    s[i]='1'
                else:
                    s[i]='0'
            return ''.join(s)
        def reverse(s):
            s=s[::-1]
            return s
        
        for i in range(n):
            s=s+'1'+ reverse(invert(s))
        return s[k-1]