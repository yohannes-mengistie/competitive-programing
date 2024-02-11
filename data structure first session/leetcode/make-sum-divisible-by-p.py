class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tot = sum(nums)
        reminder = tot%p
        if reminder == 0:
            return 0
        dic = {0:-1}
        running_sum = 0
        res = float("inf")

        for ind in range(len(nums)):
            running_sum += nums[ind]
            key = (running_sum%p - reminder)

            if key < 0:
                key +=p
            if key in dic:
                res = min(res,ind - dic[key])
            
            dic[running_sum%p] = ind

        return -1 if res >=len(nums) else res


