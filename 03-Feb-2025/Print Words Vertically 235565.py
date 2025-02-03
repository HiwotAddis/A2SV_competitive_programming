# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        lst=s.split() #["HOW","ARE","YOU"]
        max_l=max(len(word) for word in lst)
        res=[]
        for i in range(max_l):
            vert=''
            for word in lst:
                if i<len(word):
                    vert+=word[i]
                else:
                    vert+=' '
            res.append(vert.rstrip())
        return res