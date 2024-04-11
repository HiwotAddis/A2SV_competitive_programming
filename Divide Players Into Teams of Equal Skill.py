class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i=0
        j=len(skill)-1
        s=0
        if len(skill)==2:
            return skill[i]*skill[j]
        while i<j:
            if skill[i]+skill[j] != skill[i+1] +skill[j-1]:
                return -1
                break
            else:
                s+=skill[i]*skill[j]
                i+=1
                j-=1
        return s
