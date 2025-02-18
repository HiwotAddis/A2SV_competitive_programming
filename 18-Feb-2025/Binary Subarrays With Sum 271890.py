# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count={0:1}
        prefix_sum=0
        count=0
        for num in nums:
            prefix_sum+=num
            x=prefix_sum-goal
            if x in prefix_count:
                count+=prefix_count[x]
            prefix_count[prefix_sum]=prefix_count.get(prefix_sum,0)+1
        return count