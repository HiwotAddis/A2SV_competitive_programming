# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        LST=[[1,'I'],[4,'IV'],[5,'V'],[9,'IX'],[10,'X'],[40,'XL'],[50,'L'],[90,'XC'],[100,'C'],[400,'CD'],[500,'D'],[900,'CM'],[1000,'M']]
        res=''
        for val,smb in reversed(LST):
            if num//val:
                count=num//val
                num=num%val
                res+=smb*count
        return res

