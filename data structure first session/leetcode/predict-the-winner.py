class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        if len(nums)%2 == 0:
            return True
        if len(nums) == 1:
            return True
        visited = {}
        def winner(left,right,turn):
            if left > right:
                return 0
            if (left,right,turn) in visited:
                return visited[(left,right,turn)]
            res = 0
            if turn == 1:
                res = max(nums[left]+winner(left+1,right,2),nums[right]+winner(left,right-1,2))
            elif turn == 2:
                res = min(winner(left+1,right,1),winner(left,right-1,1))
            

            visited[(left,right,turn)] = res
            return res
        scoreA = winner(0,len(nums)-1,1)
        return sum(nums)-scoreA <= scoreA