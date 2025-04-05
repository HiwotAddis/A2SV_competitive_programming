# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        S=sorted(count.items(), key=lambda x:x[1] , reverse=True)
        res=[]
        for i in range(k):
            res.append(S[i][0])
        return res