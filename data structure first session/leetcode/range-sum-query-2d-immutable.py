class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prifix = []
        n = len(matrix)+1
        m = len(matrix[0])+1
        for i in range(n):
            self.prifix.append([0 for i in range(m)])
       
        for i in range(1,n):
            for j in range(1,m):
                self.prifix[i][j] = self.prifix[i-1][j] + self.prifix[i][j-1] - self.prifix[i-1][j-1] + matrix[i-1][j-1]

        print(self.prifix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prifix[row2+1][col2+1]-self.prifix[row2+1][col1] - self.prifix[row1][col2+1]+self.prifix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)