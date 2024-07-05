class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arrow=1
        last_arrow_position=points[0][1]
        for start,end in points:
            if start>last_arrow_position:
                arrow+=1
                last_arrow_position=end
        return arrow
