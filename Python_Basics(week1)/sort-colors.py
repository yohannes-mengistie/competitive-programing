class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def swap(i,j):
            nums[i],nums[j] = nums[j],nums[i]
        k,j = 0 ,len(nums)-1
        i = 0
        while i<=j:
            if nums[i] == 0:
                swap(k,i)
                k +=1
            elif nums[i] == 2:
                swap(i,j)
                j -=1
                i -=1
                
            i +=1
        return nums
            