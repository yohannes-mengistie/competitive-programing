class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def backtrack(ind):
            if len(path) == k:
                ans.append(path.copy())
                return
            for i in range(ind+1,n+1):
                path.append(i)
                backtrack(i)

                path.pop()
            
        backtrack(0)
        return ans



