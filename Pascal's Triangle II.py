class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row=[1]
        for _ in range(rowIndex):
            row=[1]+[row[j]+row[j+1] for j in range(len(row)-1)]+[1]
        return row
        
