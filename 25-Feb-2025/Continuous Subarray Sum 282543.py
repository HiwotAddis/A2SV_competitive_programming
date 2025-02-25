# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap={0:-1}
        prefix_sum=0
        for index in range(len(nums)):
            prefix_sum+=nums[index]
            remainder=prefix_sum%k
            if remainder in hashmap and index-hashmap[remainder]>=2:
                return True
            elif remainder not in hashmap:
                hashmap[remainder]=index
        return False