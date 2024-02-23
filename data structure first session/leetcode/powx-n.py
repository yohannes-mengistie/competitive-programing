class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1/self.myPow(x,-n)
        else:
            reserve = self.myPow(x,n//2)
            if n%2 == 0:
                return reserve*reserve
            else:
                return x*(reserve*reserve)
