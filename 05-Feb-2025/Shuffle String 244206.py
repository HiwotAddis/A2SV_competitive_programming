# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=[0]*len(s)
        for i in range(len(indices)):
            res[indices[indices[i]]]=s[indices[i]]
        return ''.join(res)
        