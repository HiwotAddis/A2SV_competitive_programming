# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        c=defaultdict(list)
        for path in paths:
            path=path.split(" ")
            folder=path[0]
            for s in path[1:]:
                s=s.split(".txt")
                name=s[0]
                content=s[1]
                c[content].append((folder,name))
        output=[]
        for k,v in c.items():
            if len(v)>1:
                tmp=[]
                for folder,name in v:
                    tmp.append(folder+'/'+name+".txt")
                output.append(tmp)
        return output