# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for i in operations:
            if i =='--X' or i=='X--':
                x-=1
            elif i=='++X' or i=='X++':
                x+=1
        return x