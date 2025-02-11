# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_=[str(num) for num in nums] 
        for i in range(len(str_)):
            max_idx=i
            for j in range(i+1,len(str_)):
                if str_[j]+str_[max_idx]> str_[max_idx]+str_[j]:
                    max_idx=j
            str_[i],str_[max_idx]=str_[max_idx],str_[i]
        res=''.join(str_)
        if int(res)==0:
            return "0"
        return res