class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        ans = 0
        right = len(s)-1
        while right >-1:
            if s[right] == "0":
                count +=1
            else:
                ans +=count

            right -=1
            
        return ans