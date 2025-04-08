# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        res=[]
        for i in count:
            if count[i]>1:
                res.append(i)
        for i in range(1,len(nums)+1):
            if i not in nums:
                res.append(i)
        return res