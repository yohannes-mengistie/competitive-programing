class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        index_one = []
        
        for ind in range(len(boxes)):
            ans = 0
            for j in range(len(boxes)):
                
                if boxes[j] == '1':
                    ans += abs(ind-j)
            index_one.append(ans)
        return index_one
        