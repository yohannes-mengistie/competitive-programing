class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # if sum(candidates) < target:
        #     return []
        candidates.sort()
        ans = []
        comb = []
        def dfs(ind,tot):
            if  tot == 0:
                ans.append(comb.copy())
                return
           
            if tot <= 0:
                return
            prv = -1
            for i in range(ind,len(candidates)):
                if candidates[i] == prv:
                  continue
                comb.append(candidates[i])
                dfs(i+1,tot-candidates[i])
                comb.pop()
                prv = candidates[i]
               
            
            
        dfs(0,target)
        
        return ans
       