# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        for idx,value in enumerate (nums):
            required_value=target-value
            if required_value in dict:
                return [dict[required_value],idx]
            else:
                dict[value]=idx
          
             
                  
