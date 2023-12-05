class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        initial_dis = abs(target[0])+abs(target[1])
        for gohs in ghosts:
            ans = abs(gohs[0]-target[0])+abs(gohs[1]-target[1])
            if ans <= initial_dis:
                return False
        return True
        
