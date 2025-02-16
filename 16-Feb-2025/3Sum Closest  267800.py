# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest=float('inf')
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                Sum=nums[i]+nums[l]+nums[r]
                if Sum==target:
                    return Sum
                elif Sum>target:
                    r-=1
                else:
                    l+=1
                if abs(target-Sum)<abs(target-closest):
                    closest=Sum
        return closest
                