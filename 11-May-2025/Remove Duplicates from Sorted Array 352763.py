# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=r=1
        while r<len(nums):
            if nums[r] != nums[r-1]:
                nums[l]=nums[r]
                l+=1
            r+=1
        return l