# Problem: Broken Calculator - https://leetcode.com/problems/broken-calculator/description/

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        operation=0
        while target>startValue:
            if target%2 ==0:
                target//=2
            else:
                target+=1
            operation+=1
        return operation+startValue-target