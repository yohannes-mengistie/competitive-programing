class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = list(s.split())
        ma = 0
        
        for i in s:
            ma = max(len(i),ma)
        for i in range(len(s)):
            if len(s[i]) < ma:
                s[i] = s[i] + " " * (ma-len(s[i]))  
        
        
        
        ans = []
        for i in range(ma):
            cur = ""
            for j in range(len(s)):
                cur +=s[j][i]
            ans.append(cur.rstrip())
        return ans
                