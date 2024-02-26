class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def dfs(ind):
            if ind >= len(nums) :
              
                ans.append(cur.copy())
                return
            cur.append(nums[ind])
            dfs(ind+1)
            cur.pop()
            dfs(ind+1)
        
        cur = []
        ans=[]
        dfs(0)
        ans.sort()
        result = []
        for i in ans:
            if i not in result:
                result.append(i)

        return result
