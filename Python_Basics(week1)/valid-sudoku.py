class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans = []
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != '.':
                   ans += [(i,cur),(cur,j),(i//3,j//3,cur)]

        return len(ans) == len(set(ans))