class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        ans = 0
        total = sum(distance)
        if start < destination:
            ans = sum(distance[start:destination])
        else:
            ans = sum(distance[destination:start])        
        min_dis = min(ans,abs(total-ans))
        return min_dis

