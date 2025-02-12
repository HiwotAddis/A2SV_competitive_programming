# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        sorted_= dict(sorted(count.items(),key=lambda x:x[1],reverse=True))
        res=''
        for i in sorted_:
            res+=i*sorted_[i]
        return res
        