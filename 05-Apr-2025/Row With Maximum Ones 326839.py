# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        idx=float('inf')
        ones=0
        for i in range(len(mat)):
            count=mat[i].count(1)
            if count>ones:
                ones=count
                idx=i
            elif count==ones:
                idx=min(idx,i)
        if idx==float('inf'):
            idx=0
        return [idx,ones]