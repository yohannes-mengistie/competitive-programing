class Solution:
    def totalMoney(self, n: int) -> int:
        money = 0
        saving = [1,2,3,4,5,6,7]
        for day in range(n):
            money +=saving[day%7]
            saving[day%7] +=1

        return money
        