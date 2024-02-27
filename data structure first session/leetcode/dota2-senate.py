class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dq = deque([i for i in range(len(senate)) if senate[i]=="D"])
        rq = deque([i for i in range(len(senate)) if senate[i]=="R"])
      
        while dq and rq:
            first = dq.popleft()
            second = rq.popleft()
            if second < first:
                rq.append(first+len(senate))
            else:
                dq.append(second+len(senate))
            
        
        return "Radiant" if rq else "Dire"

