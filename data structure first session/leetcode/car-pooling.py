class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prifix = [0]*1001

        for trip in trips:
            num_pas = trip[0]
            start = trip[1]
            end = trip[2]

            prifix[start] +=num_pas
            prifix[end] -=num_pas

        for  i in range(1,1001):
            prifix[i] +=prifix[i-1]

        for trip in trips:
            start = trip[1]
            end = trip[2]

            if prifix[start]>capacity or prifix[end] > capacity:
                return False
        return True