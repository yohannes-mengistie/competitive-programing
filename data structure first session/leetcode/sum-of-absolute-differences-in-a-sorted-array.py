class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prifix = [0]*len(nums)
        tot = 0
        for i in range(len(nums)):
            tot += nums[i]
            prifix[i] = tot
        post = [0]*len(nums)
        tot = 0
        for i in range(len(nums)-1,-1,-1):
            tot += nums[i]
            post[i] = tot
        
        for j in range(len(nums)):
            if j == 0:
                nums[j] = post[j+1] - nums[j]*(len(nums)-j-1)
            elif j == len(nums)-1:
                nums[j] = nums[j]*(j) - prifix[j-1]
            else:
                nums[j] = (nums[j]*(j) - prifix[j-1]) +  (post[j+1] - nums[j]*(len(nums)-j-1))


                
        return nums
