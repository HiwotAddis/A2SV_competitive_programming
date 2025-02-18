# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols=len(matrix[0])
        rows=len(matrix)
        for i in range(rows):
            for j in range(i+1,cols):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(rows):
            matrix[i]=matrix[i][::-1]
        return matrix
