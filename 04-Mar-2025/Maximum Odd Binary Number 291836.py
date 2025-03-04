# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones=s.count('1')
        zeros=s.count('0')
        res=''
        if ones==1:
            res+='0'*zeros+'1'
        else:
            res+='1'*(ones-1)+'0'*zeros+'1'
        return res