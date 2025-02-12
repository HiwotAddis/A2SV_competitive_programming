# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx={}
        for i in range(len(s)):
            last_idx[s[i]]=i
        res=[]

        start=end=0
        for i in range(len(s)):
            end=max(end,last_idx[s[i]])
            if i ==end:
                res.append(end-start+1)
                start=i+1
                
        return res