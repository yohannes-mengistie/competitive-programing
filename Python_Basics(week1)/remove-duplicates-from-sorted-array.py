class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            left = 1 ; right = 1
            res = set(nums)
            n = len(res)
            while right < len(nums):
                if nums[right]!=nums[left-1]:
                    nums[left] = nums[right]
                    left +=1

                right +=1 
            i = n
            while i < len(nums):
                nums[i] = "_"
                i +=1



                           

            return n