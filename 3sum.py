class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        for i in range(len(nums)):
            prev=nums[i]
            l=i+1
            r=len(nums)-1
            while l<r:
                val=nums[l]+prev+nums[r]
                if val >0:
                    r-=1
                elif val<0:
                    l+=1
                else:
                    ans.add((prev,nums[l],nums[r]))
                    l+=1
        return ans
