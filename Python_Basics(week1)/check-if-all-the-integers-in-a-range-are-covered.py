class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        union_set=set()
        for x,y in ranges:
            for num in range(x,y+1):
                union_set.add(num)
            
        
        for num in range(left,right+1):
            if num not in union_set:
                return False
        return True