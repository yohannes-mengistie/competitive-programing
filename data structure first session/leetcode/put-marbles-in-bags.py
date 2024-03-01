class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        prefix = []
        for i in range(len(weights)-1):
            prefix.append(weights[i] + weights[i+1])
        prefix.sort()
       
        if k-1 == 0:
            return 0
        max_score = sum(prefix[-k+1:])
        min_score = sum(prefix[:k-1])
        return max_score - min_score
        