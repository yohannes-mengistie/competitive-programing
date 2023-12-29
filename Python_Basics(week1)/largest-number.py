class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for ind in range(len(nums)):
        
            nums[ind] = str(nums[ind])
        for i in range(len(nums)):
            for ind in range(1,len(nums)):
                if nums[ind-1] + nums[ind] < nums[ind]+nums[ind-1]:
                    nums[ind-1],nums[ind] = nums[ind],nums[ind-1]
        result = "".join(nums)
        return  str(int(result))