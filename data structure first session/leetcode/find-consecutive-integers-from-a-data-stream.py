class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = []
        self.counter = 0
        self.pointer = 0

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value :
            if len(self.queue) - self.pointer >=self.k:
                return True
            else:
                return False
        elif num != self.value:
            self.pointer = len(self.queue)
            return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)