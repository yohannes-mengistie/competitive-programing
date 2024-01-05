class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        dic = {}
        nums.sort()
        for i in range(len(nums)):
            left = i+1 ; right = len(nums)-1

            while left < right:
                temp = nums[left] + nums[i] + nums[right]
                res = abs(target-temp)
                dic[res] = temp
                if temp > target:
                    right -=1
                elif temp <= target:
                    left +=1
            
        for key in sorted(dic):
            return dic[key]