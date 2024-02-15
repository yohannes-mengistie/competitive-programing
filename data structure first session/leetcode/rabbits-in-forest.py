import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = defaultdict(int)
        ans = 0
        for answer in answers:
            dic[answer] +=1
        
        for key,value in dic.items():
            ans += math.ceil(value/(key+1))*(key+1)

        return ans

