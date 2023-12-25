class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
            firs = inf
            second = inf
            third = inf

            for value in nums:
                if value > second:
                    return True
                elif value <firs:
                    firs = value

                elif value > firs and value < second:
                    second = value
                
            return False
                
            
                

            
        