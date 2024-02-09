class Solution:
    def numberOfWays(self, s: str) -> int:
        count_zero = s.count("0")
        count_one = s.count("1")
        
        countz = 0
        ans1 =0 
        for i in range(len(s)):
            
            if s[i] =="0":
                countz +=1
            elif s[i] == "1" and i>0 and i < len(s)-1:
                ans1 += countz*(count_zero-countz)

        countr = 0
        ans2 = 0
        for j in range(len(s)):
            
            if s[j] =="1":
                countr  +=1
            elif s[j] == "0" and j  > 0 and j < len(s)-1:
                ans2 += countr*(count_one-countr)
        print(ans1)
        print(ans2)
        ans = ans1 + ans2

        return ans


       

