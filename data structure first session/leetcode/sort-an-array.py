def merg(left_half,right_half):
            arr = []
            i = 0
            j = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr.append(left_half[i])
                    i +=1
                else:
                    arr.append(right_half[j])
                    j +=1
            while i < len(left_half):
                arr.append(left_half[i])
                i +=1
            while j < len(right_half):
                arr.append(right_half[j])
                j +=1
            return arr
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergSort(left,right,nums):
            if left == right:
                return [nums[left]]
            mid = (left+right)//2
            left_half = mergSort(left,mid,nums)
            right_half = mergSort(mid+1,right,nums)
            return merg(left_half,right_half)
            
          
           
        return mergSort(0,len(nums)-1,nums)
