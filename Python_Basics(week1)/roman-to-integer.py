class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s = s[::-1]
        ans = 0
        cur = hashmap[s[0]]
        for i in s:
            if cur < hashmap[i]:
                ans += hashmap[i]
                cur = hashmap[i]
            elif cur > hashmap[i]:
                ans -= hashmap[i]
            else:
                ans += hashmap[i]
            
           
        return ans
    