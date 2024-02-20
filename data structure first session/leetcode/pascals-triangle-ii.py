class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prvRow = self.getRow(rowIndex-1)
        row = [1]
        for i in range(1,len(prvRow)):
            row.append(prvRow[i-1]+prvRow[i])
        row.append(1)
        return row