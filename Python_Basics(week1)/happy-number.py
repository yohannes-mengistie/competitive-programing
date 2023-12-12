class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquares(n):
            ans = 0
            while n > 0:
                cur = n%10
                ans += (cur**2)
                n = n//10
            return ans
        res = set()
        while n not in res:
            res.add(n)
            n = sumSquares(n)
            if n == 1:
                return True
        return False


