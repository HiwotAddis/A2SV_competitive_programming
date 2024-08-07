class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start==len(nums):
                res.append(nums[:])
            for i in range(start,len(nums)):
                nums[i],nums[start]=nums[start],nums[i]
                backtrack(start+1)
                nums[i],nums[start]=nums[start],nums[i]
        res=[]
        backtrack(0)
        return res
