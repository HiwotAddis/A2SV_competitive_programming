# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        k=k%len(nums)
        nums[:k]=nums[:k][::-1]
        nums[k:]=nums[k:][::-1]