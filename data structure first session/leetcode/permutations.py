class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def backtrac(current):
            if len(current) == len(nums):
                ans.append(current.copy())
                return
            for num in nums:
                if num not in current:
                    current.append(num)
                    backtrac(current)
                    current.pop()
        
        for num in nums:
            current = [num]
            backtrac(current)
        return ans