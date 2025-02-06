# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        count=Counter(nums)
        for i in count:
            if count[i]>len(nums)/3:
                res.append(i)
        return res