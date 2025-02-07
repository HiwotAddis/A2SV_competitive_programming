# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res=[]
        in_block=False
        for line in source:
            if not in_block:
                newline=[]
            i=0
            while i<len(line):
                if line[i:i+2]=='/*' and not in_block:
                    in_block=True
                    i=i+1
                elif line[i:i+2]=='*/' and in_block:
                    in_block=False
                    i+=1
                elif not in_block and line[i:i+2]=='//':
                    break
                elif not in_block:
                    newline.append(line[i])
                i+=1
            if not in_block and newline:
                res.append(''.join(newline))
        return res
                

