class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = set()
        
        nums.sort()
        for i,val in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l= i+1
            r = len(nums)-1
            while l<r:
               if (val+nums[l]+nums[r]) < 0:
                   l +=1
                   
               elif (val +nums[l] +nums[r]) > 0:
                   r -=1
               else:
                   
                    output.add((val,nums[l],nums[r]))
                    l +=1
                   
        
        return output