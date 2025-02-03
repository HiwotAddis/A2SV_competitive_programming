# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers=[]
        answer=[[],[]]
        for w,l in matches:
            losers.append(l)
        dict_l=Counter(losers)

        for w,l in matches:
            if w not in dict_l and w not in answer[0]:
                answer[0].append(w)
        for key in dict_l:
            if dict_l[key] ==1:
                answer[1].append(key)
        answer[0].sort()
        answer[1].sort()
        return answer