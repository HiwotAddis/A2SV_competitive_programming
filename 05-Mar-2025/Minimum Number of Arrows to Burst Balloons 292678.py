# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        max_=points[0][1]
        arrow=1
        for i in range(1,len(points)):
            if points[i][0]>max_:
                max_=points[i][1]
                arrow+=1
        return arrow