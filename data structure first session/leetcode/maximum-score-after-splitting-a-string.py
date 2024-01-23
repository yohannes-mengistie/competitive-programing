class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        tot = 0
        for num in s:
            tot += int(num)
        tot +=left
        ans = 0
        for i in range(len(s)-1):
            
            if int(s[i]) == 1:
                tot -=1
            else:
                left +=1
            ans = max(ans,left + tot)

        return ans