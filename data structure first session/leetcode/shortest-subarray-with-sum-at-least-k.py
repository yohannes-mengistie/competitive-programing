class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q = deque([])
        tot = [0]
        for n in nums:
            tot.append(tot[-1]+n)

        window = float("inf")
        for i , n in enumerate(tot):
            while q and tot[q[-1]] >= n:
                q.pop()
            while q and n - tot[q[0]]>= k:
                
                window = min(window,i-q.popleft())
            q.append(i)
            #print(q)
        
        if window != inf:
           return window
        return -1
            
           

