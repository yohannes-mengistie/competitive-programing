class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
       ans = 0
       poww = 16
       while poww >= 0:
           cur =  (3**poww)
           if cur+ans < n:
              ans += cur
           elif ans+cur == n:
               return True
           poww -=1
       return False



