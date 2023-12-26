class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        sum1 = 0
        sum2 = 0
        i = j= 0
        while i <m and j<n:
            sum1 += mat[i][j]
            i +=1
            j +=1
        row = 0 ; column = n-1
        while row < m and  column >= 0:
            sum2 += mat[row][column]
            row +=1
            column -=1

        if m%2!=0 and m >1:
            k = ceil(m/2)
            
            return sum1+sum2-mat[k-1][k-1]
        elif m==1:
            return mat[0][0]
        else:
            return sum1+sum2

     
      ##  1,2,3,4 4
        #   2 3 4 6 4
        #   3 5 6 7 4
        #   2 4 3 4 3
        #   3 4 6 6 3