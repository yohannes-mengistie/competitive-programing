from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        counter = Counter(arr)
        cur = []
        for key , value in counter.items():
            cur.append([value,key])
        cur = sorted(cur,reverse=True)
        return cur[0][1]
