# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def merge(self,left_sum,right_sum):
        i=j=0
        res=[]
        while i <len(left_sum) and j < len(right_sum):
            if left_sum[i]<right_sum[j]:
                res.append(left_sum[i])
                i+=1
            else:
                res.append(right_sum[j])
                j+=1
        while i<len(left_sum):
            res.append(left_sum[i])
            i+=1
        while j<len(right_sum):
            res.append(right_sum[j])
            j+=1
        return res
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)>1:
            mid=len(nums)//2
            left=nums[:mid]
            right=nums[mid:]

            left_sort=self.sortArray(left)
            right_sort=self.sortArray(right)
            return self.merge(left_sort, right_sort)
        return nums
    