class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prifix = [0]*(len(nums)+1)
        for request in requests:
            start = request[0]
            end = request[1]

            prifix[start] += 1
            if end < len(prifix):
               prifix[end+1] -=1

        for ind in range(1,len(prifix)):
            prifix[ind]+=prifix[ind-1]

        prifix = sorted(prifix,reverse = True)
        nums = sorted(nums,reverse =True)
        ans = 0
       
        for i in range(len(nums)):
            ans += prifix[i]*nums[i] 

        return ans%(10**9+7)

