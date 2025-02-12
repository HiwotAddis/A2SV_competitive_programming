# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans=[]
        i=0
        j=len(skill)-1
        target=skill[i]+skill[j]
        res=0
        while i<j:
            if skill[i]+skill[j]==target:
                ans.append((skill[i],skill[j]))
                i+=1
                j-=1
            else:
                return -1 
        for l,r in ans:
            res+=l*r  
        return res
