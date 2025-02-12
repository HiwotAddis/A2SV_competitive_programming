# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        lst=[]
        i=0
        j=len(height)-1
        while i<j:
            if height[i]<height[j]:
                area=height[i]*(j-i)
                i+=1
            else:
                area=height[j]*(j-i)
                j-=1
            lst.append(area)
        return max(lst)
            