# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        S=sum(i for i in nums if i%2==0)
        ans=[]
        for val , idx in queries:
            if nums[idx]%2==0 and (nums[idx]+val)%2!=0:
                S-=nums[idx]
            elif nums[idx]%2==0 and (nums[idx]+val)%2==0:
                S+=val
            elif (nums[idx]%2!=0 and (nums[idx]+val)%2==0):
                S+=(nums[idx]+val)

            nums[idx]=nums[idx]+val


            ans.append(S)
        return ans