class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
            nums.sort()
            count = 0 ; cur = nums[0] ; ans = 0

            for ind in range(1,len(nums)):
                if cur != nums[ind]:
                    count +=1
                    ans +=count
                    cur = nums[ind]

                else:
                    ans +=count
            return ans
