class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
        n = x
        ans = 0
        while x >0:
            rem = x%10
            x  = x//10
            ans = (ans*10) + rem
            
        
        if ans == n:
            return True
        else:
            return False

