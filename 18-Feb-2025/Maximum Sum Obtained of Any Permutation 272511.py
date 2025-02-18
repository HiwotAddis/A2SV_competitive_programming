# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n=len(nums)
        prefix_sum=[0]*(n+1)
        for l,r in requests:
            prefix_sum[l]+=1
            prefix_sum[r+1]-=1
        for i in range(1,n):
            prefix_sum[i]+=prefix_sum[i-1]
        prefix_sum.pop()
        prefix_sum.sort()
        nums.sort()
        max_=sum(f*i for f,i in zip(prefix_sum,nums))%(10**9 + 7)
        return max_