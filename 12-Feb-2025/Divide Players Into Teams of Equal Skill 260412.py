# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        i=0
        j=len(skill)-1
        chemo=0
        skill.sort()
        target=skill[i] +skill[j]
        while i<j:
            if skill[i]+skill[j]==target:
                chemo+=skill[i]*skill[j]
            else:
                return -1
            i+=1
            j-=1
        return chemo