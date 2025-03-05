# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
        rabbits=0
        for ans,frq in count.items():
            grp_size=ans+1
            no_ofGrp=ceil(frq/grp_size)
            rabbits+=no_ofGrp*grp_size
        return rabbits
        