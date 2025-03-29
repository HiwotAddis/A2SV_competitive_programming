# Problem: Search Insert Position - https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        ans=len(nums)
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                ans=mid
                break
            elif nums[mid]<target:
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans