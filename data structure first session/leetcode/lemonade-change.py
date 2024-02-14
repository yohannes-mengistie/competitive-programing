class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        amount5 = 0
        amount10 = 0
        
        for i in range(len(bills)):
            if bills[i] == 5:
                amount5 +=1
            elif bills[i] == 10:
                if amount5 ==0:
                    return False
                amount10 +=1
                amount5 -=1
            else:
                if amount5>=1 and amount10>=1:
                    amount5 -=1
                    amount10 -=1
                elif amount5 >= 3:
                    amount5 -= 3
                else:
                    return False
           
        return True

            