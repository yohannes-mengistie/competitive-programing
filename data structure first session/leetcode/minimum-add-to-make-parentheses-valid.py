class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = 0
        ans= 0
        for brackt in s:
            if brackt == "(":
                stack +=1
            elif brackt == ")" and stack == 0:
                ans +=1
            else:
                stack -=1
            
        if stack:
            ans +=stack
        return ans


