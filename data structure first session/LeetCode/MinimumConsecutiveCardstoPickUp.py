class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        count = len(cards)+1
        dic = {}
        left = 0
        for i in range(len(cards)):
            if cards[i] not in dic:
                dic[cards[i]] = 1
            elif cards[i] in dic:
                dic[cards[i]] +=1
            
            while dic[cards[i]] >= 2:
                count = min(count,i-left+1)
                dic[cards[left]] -=1
                left +=1
        if count != len(cards)+1:
           return count

        else:
            return -1