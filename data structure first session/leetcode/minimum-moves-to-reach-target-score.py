class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0:
            return target-1
        elif target == 1:
            return 0
        else:
            current = target
            ans = 0
            while maxDoubles >0 and current > 1:
                if current%2!=0:
                    current -=1

                else:
                    current = current // 2
                    maxDoubles -=1
                ans +=1
            if current > 1:
                ans +=current-1
            return ans
            

             

