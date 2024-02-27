class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q = sorted(deque(deck))
        ans = deque()
        for i in range(len(q)):
            temp = q.pop()
            if len(ans) > 0:
                cur = ans.pop()
                ans.appendleft(cur)
            ans.appendleft(temp)
        
        return ans