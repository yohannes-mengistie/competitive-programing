class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        def pow(x,n):
            if n == 0:
                return 1
            else:
                reserve = pow(x,n//2)
                if n%2 == 0:
                    return (reserve*reserve) % mod
                else:
                    return (x*reserve*reserve) % mod
       

        even = pow(5,(n//2)+(n%2))
        odd = pow(4,n//2)
        ans = even*odd
        return ans%mod