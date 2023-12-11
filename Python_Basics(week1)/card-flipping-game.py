class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        s = set(fronts+backs)
        for ind in range(len(backs)):
            if fronts[ind] == backs[ind] and fronts[ind] in s:
                s.remove(fronts[ind])
        if len(s) == 0:
            return 0
        else:
           return min(s)
        
