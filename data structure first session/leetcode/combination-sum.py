class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []
        def backtrack(ind,num):
            if  num == target:
                ans.append(path.copy())
                return
            if ind >= len(candidates) or num > target:
                return
            path.append(candidates[ind])
            backtrack(ind,num +candidates[ind] )
            path.pop()
            backtrack(ind+1,num)
            
        backtrack(0,0)
        return ans
