# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row=len(matrix)
        col=len(matrix[0])
        self.prefix_sum=[[0]*(col+1) for _ in range(row+1)]
        for r in range(row):
            for c in range(col):
                self.prefix_sum[r+1][c+1]=self.prefix_sum[r+1][c]+self.prefix_sum[r][c+1]-self.prefix_sum[r][c]+matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_sum[row2+1][col2+1]-self.prefix_sum[row2+1][col1]-self.prefix_sum[row1][col2+1]+self.prefix_sum[row1][col1]