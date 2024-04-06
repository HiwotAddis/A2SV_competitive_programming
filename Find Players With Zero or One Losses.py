class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser_mp={}
        for i in matches:
            if i[0] not in loser_mp:
                loser_mp[i[0]]=0
            if i[1] not in loser_mp:
                loser_mp[i[1]]=1
            else:
                loser_mp[i[1]]+=1
        ans=[[],[]]
        for i in loser_mp:
            if loser_mp[i] ==0:
                ans[0].append(i)
            elif loser_mp[i]==1:
                ans[1].append(i)
        ans[0].sort()
        ans[1].sort()
        return ans
