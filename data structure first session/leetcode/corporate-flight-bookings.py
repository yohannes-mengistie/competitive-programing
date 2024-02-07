class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0]*(n)
        for book in bookings:
            a,b,c = book
            if a <= n:
              arr[a-1] += c
            if b < n:
              arr[b] -=c
        for i in range(1,len(arr)):
            arr[i] += arr[i-1]

        return arr