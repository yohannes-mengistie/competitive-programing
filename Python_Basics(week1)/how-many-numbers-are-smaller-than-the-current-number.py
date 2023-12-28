class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = {}
        
        new = sorted(nums)
        for ind in range(len(new)):
            if new[ind] not in dic:
                dic[new[ind]] = ind

        for i in range(len(nums)):
            nums[i] = dic[nums[i]]
        
        return nums