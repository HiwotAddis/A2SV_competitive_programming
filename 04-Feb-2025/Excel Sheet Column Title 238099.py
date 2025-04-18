# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans=''
        while columnNumber>0:
            columnNumber-=1
            ans+=chr(columnNumber%26 +ord('A'))
            columnNumber//=26
        return ans[::-1]