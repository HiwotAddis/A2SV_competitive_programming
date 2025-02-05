# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        count=Counter(nums)
        for i in count:
            if count[i]>1:
                res.append(i)
        return res