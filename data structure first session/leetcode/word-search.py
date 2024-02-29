class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col = len(board),len(board[0])
        path = set()
        def backtrack (r,c,i):
            if i == len(word):
                return True
            if   (0 > r or r >= row or 0 > c  or c >= col) or ((r,c) in path) or (board[r][c] != word[i]):
                return False
            path.add((r,c))
            if backtrack(r,c-1,i+1) or  backtrack(r,c+1,i+1) or  backtrack(r-1,c,i+1) or  backtrack(r+1,c,i+1):
                return True
            path.remove((r,c))
        for i in range(row):
            for j in range(col):
                if backtrack(i,j,0):
                    return True
        return False
        
            
