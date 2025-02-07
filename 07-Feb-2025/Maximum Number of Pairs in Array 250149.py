# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dict=Counter(nums)
        pairs=leftover=0
        for val in dict.values():
            if val%2==0:
                pairs+=val//2
            else:
                pairs+=val//2
                leftover+=val%2
        return [pairs,leftover]
