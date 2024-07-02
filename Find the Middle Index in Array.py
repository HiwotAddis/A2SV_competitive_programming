class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ps=sum(nums)
        left=0
        for i,num in enumerate(nums):
            if left==ps-num-left:
                return i
            left+=num
        return -1
