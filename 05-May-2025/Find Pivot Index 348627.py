# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]

        for i in range(n):
            left = prefix[i - 1] if i > 0 else 0
            right = suffix[i + 1] if i < n - 1 else 0
            if left == right:
                return i

        return -1