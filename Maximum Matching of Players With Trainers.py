class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        i=0
        players.sort()
        trainers.sort()
        count=0
        for t in trainers:
            if i<len(players) and players[i]<=t:
                count+=1
                i+=1
        return count
