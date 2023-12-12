class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.pair = {}
        for i in range(1,n+1):
            self.pair[i] = 0
        self.pointer = 1
        
    def insert(self, idKey: int, value: str) -> List[str]:
        ans = []
        self.pair[idKey] = value
        while self.pointer <= self.n  and self.pair[self.pointer]:
           
            ans.append(self.pair[self.pointer])
            self.pointer +=1
        return ans
            



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)