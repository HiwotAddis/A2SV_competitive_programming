# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        lst=[]
        for s,e in ranges:
            for i in range(s,e+1):
                lst.append(i)
        for i in range(left,right+1):
            if i not in lst:
                return False
        return True
        