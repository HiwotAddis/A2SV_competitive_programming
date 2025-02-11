# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d={}
        res=[]
        n=sorted(nums,reverse=True)
        for i in range(len(n)):
            count=0
            for j in range(i+1,len(n)):
                if n[j]<n[i]:
                    count+=1
            d[n[i]]=count
        for num in nums:
            res.append(d[num])
        return res