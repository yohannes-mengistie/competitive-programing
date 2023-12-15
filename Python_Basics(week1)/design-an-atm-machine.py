class ATM:

    def __init__(self):
       self.notes = [20,50,100,200,500] 
       self.notes_freq = [0]*5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.notes_freq[i] +=banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        remaning = [0]*5
        for ind in range(4,-1,-1):
            used = min(self.notes_freq[ind] , amount//self.notes[ind])
            remaning[ind] = used
            
            amount -= (self.notes[ind]*used)
        if amount :
            return [-1]

        for ind in range(5):
            self.notes_freq[ind] -= remaning[ind]
        return remaning
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)