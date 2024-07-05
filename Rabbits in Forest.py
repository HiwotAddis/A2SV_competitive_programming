class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
        total=0
        for ans,freq in count.items():
            group_size=ans+1
            group=(freq + group_size - 1) // group_size
            total+=group_size*group
        return total
