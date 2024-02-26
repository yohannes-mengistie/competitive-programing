class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(ind):
            if ind >= len(nums) :
                ans.append(curr.copy())
                return
            # taking current element
            curr.append(nums[ind])
            helper(ind+1)
            
            # not taking current element
            curr.pop()
            helper(ind+1)
            

        curr = []
        ans = []
        helper(0)
        return ans