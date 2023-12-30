class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        tot = 0
        i = len(piles)-2
        j = 0

        while j < len(piles)//3:
            tot += piles[i]
            j +=1
            i -=2

        return tot
        


