class Solution:
    def maxArea(self, height: List[int]) -> int:
        lst=[]
        i=0 
        j = len(height)-1
        while (i < j):
            if height[i] <= height[j]:
                res = height[i] * (j - i)
                i += 1

            else:
                res = height[j] * (j - i)
                j -= 1
            lst.append(res)
        return max(lst)
