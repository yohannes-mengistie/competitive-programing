class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range (len(grid)):
            for j in range(len(grid[i])):
                temp = grid[i][j]
                A = (i-1,j-1)
                B = (i-1,j)
                C= (i-1,j+1)
                E = (i+1,j-1)
                F = (i+1,j)
                G = (i+1,j+1)
                arr = [A,B,C,E,F,G]
                for x,y in arr:
                    if x >=0 and x<len(grid) and y >=0 and y<len(grid[i]):
                        temp +=grid[x][y]
                    else:
                        break
                else:
                    ans = max(ans,temp)
        return ans
