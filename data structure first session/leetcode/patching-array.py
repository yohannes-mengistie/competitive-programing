class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
            pref = 0
            pach_count = 0
            last_ind = 0
            i = 1
            while i < n+1:
                while last_ind < len(nums) and i >= nums[last_ind]:
                    pref +=nums[last_ind]
                    last_ind +=1
                if pref < i:
                    pach_count +=1
                    pref +=i
                i = pref+1

            return pach_count
                


                



            

           
            
            

            
            
            


