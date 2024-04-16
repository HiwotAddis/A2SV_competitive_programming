class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=''
        j=0
        for i ,l in enumerate(s):
            if j<len(spaces) and i==spaces[j]:
                res+=" "+l
                j+=1
            else:
                res+=l
        return res
