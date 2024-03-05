class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        node = self.kthGrammar(n-1,math.ceil(k/2))
        check = k%2 == 1
        if node == 1:
            return 1 if check else 0
        else:
            return 0 if check else 1
    