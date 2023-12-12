class UndergroundSystem:

    def __init__(self):
        self.check = {}
        self.totalTime = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start,time = self.check[id]
        temp = (start,stationName)
        if temp not in self.totalTime:
            self.totalTime[temp] = [0,0]
        self.totalTime[temp][0] += (t-time)
        self.totalTime[temp][1] +=1



    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total,count = self.totalTime[(startStation,endStation)]
        return total/count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)