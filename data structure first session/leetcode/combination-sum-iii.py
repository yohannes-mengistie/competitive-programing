class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = []
        comb = []
        def backtrack(ind,num,n):
            if len(comb) == k and num == n:
                ans.append(comb.copy())
                return
            if num > n:
                return
            for i in range(ind,10):
                if len(comb) > 1 and comb[-1] == comb[-2]:
                    continue
                comb.append(i)
                backtrack(i+1,num+i,n)
                comb.pop()
        backtrack(1,0,n)
        return ans