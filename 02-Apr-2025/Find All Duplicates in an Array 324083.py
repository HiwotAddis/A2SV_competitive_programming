# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums=Counter(nums)
        res=[]
        for num in nums:
            if nums[num]==2:
                res.append(num)
        return res