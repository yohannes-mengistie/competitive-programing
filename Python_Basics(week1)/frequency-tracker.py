class FrequencyTracker:

    def __init__(self):
        self.frequency = defaultdict(int)
        self.number = defaultdict(int)

    def add(self, number: int) -> None:
        self.number[number] +=1
        f = self.number[number]
        self.frequency[f] += 1
        self.frequency[f-1] -=1


    def deleteOne(self, number: int) -> None:
        if self.number[number]:
            self.number[number] -=1
            f = self.number[number]
            self.frequency[f] +=1
            self.frequency[f+1] -=1 

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency[frequency] > 0
    
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)