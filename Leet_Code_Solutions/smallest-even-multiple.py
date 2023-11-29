class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        flag = True
        while flag:
            if n%2==0:
                return n
            else:
                return n*2
                