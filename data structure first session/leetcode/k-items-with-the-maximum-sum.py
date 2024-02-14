class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        if k <= numOnes:
            ans = k
        elif k > numOnes and numOnes + numZeros > k:

            
            ans = numOnes

        else:
            ans = numOnes -( k-(numOnes + numZeros))

        return ans
