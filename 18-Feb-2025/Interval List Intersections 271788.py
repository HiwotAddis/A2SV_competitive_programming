# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res=[]
        i=j=0
        while i<len(firstList) and j<len(secondList):
            s1,e1=firstList[i]
            s2,e2=secondList[j]
            start=max(s1,s2)
            end=min(e1,e2)
            if start<=end:
                res.append([start,end])
            if e1<e2:
                i+=1
            else:
                j+=1
        return res