# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=[str(i) for i in digits]
        num=''.join(digits)
        num=str(int(num)+1)
        digits=list(num)
        digits=[int(i) for i in digits]
        return digits