class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
            ans = 0
            ma = 0
            count = 0
            for ind in flips:
                #count += (ind -1)
                if ind > ma:
                    temp = ind-ma-1
                    count +=temp
                    ma = ind
                elif ind<ma:
                    count -=1
                if count == 0:
                    ans +=1
            return ans
                


