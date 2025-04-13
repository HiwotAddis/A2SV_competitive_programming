# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows=len(grid)
        cols=len(grid[0])
        direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    for dr,dc in direc:
                        new_row=row+dr
                        new_col=col+dc
                        if new_row<0 or new_row>=rows or new_col<0 or new_col>=cols or grid[new_row][new_col]==0:
                            perimeter+=1
        return perimeter