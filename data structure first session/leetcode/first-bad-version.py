# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while left <right:
            midle = (left+right)//2
            if isBadVersion(midle) :
                right = midle
            else:
                left = midle+1
        return left
            