class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prifix = 0
        ans = 0
        dic = {0:1}
        for num in nums:
            prifix +=num

            if prifix-goal in dic:
                ans += dic[prifix-goal]

            if prifix in dic:
                dic[prifix] +=1
            else:
                dic[prifix] = 1
        return ans
