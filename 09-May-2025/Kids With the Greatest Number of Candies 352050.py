# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        Max=max(candies)
        res=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=Max:
                res.append(True)
            else:
                res.append(False)
        return res