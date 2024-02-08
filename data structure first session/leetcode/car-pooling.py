class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxx = float("-inf")
        for i in range(len(trips)):
            maxx = max(maxx,trips[i][2])
        prifix = [0]*(maxx+1)

        for trip in trips:
            i,j,k = trip
            for n in range(j,k):
                prifix[n] += i

        ans = max(prifix)
        if ans > capacity:
            return False
        else:
            return True
