class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix = [0]
        tot = 0
        for i in customers:
            if i == "Y":
                tot +=0
            elif i == "N":
                tot +=1

            prefix.append(tot)
        
        sufix = [0]*(n+1)
        tot = 0
        for i in range(n-1,-1,-1):
            if customers[i] == "N":
                tot +=0
            else:
                tot +=1
            sufix[i] = tot
        sufix = sufix 
        res = float("inf")
        ind = float("inf")
        for i in range(n+1):
            summ = prefix[i] + sufix[i]
            if summ < res :
                ind = i
                res = summ
        return ind
            

