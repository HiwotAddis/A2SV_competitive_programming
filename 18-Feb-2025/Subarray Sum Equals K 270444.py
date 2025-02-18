# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count={0:1}
        prefix_sum=0
        count=0
        for num in nums:
            prefix_sum+=num
            x=prefix_sum-k
            if x in prefix_count:
                count+=prefix_count[x]
            prefix_count[prefix_sum]=prefix_count.get(prefix_sum,0)+1
        return count