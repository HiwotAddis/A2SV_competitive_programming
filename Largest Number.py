class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=[str(i) for i in nums]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]>nums[j]+nums[i]:
                    continue
                else:
                    nums[i],nums[j]=nums[j],nums[i]
        result=''.join(nums)
        if int(result)==0:
            return '0'
        return result
