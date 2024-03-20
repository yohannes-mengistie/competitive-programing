class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        sorted_map = sorted(count.items(),key = lambda x: (-x[1],x[0]))
        ans = []
        i = 0
        while k >0:
            ans.append(sorted_map[i][0])
            k -=1
            i +=1
        return ans