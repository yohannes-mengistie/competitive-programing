class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        queue = deque([i for i in range(n)])
        duration = 0

        while queue:
            for j in range(n):
                node = queue.popleft()
                tickets[node] -=1
                if tickets[node] >= 1:
                    queue.append(node)
                duration +=1
                if tickets[k] == 0:
                    return duration



