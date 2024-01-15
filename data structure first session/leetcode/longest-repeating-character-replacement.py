class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic=defaultdict(int)
        left = 0
        maxF = 0
        for j in range(len(s)):
            dic[s[j]] +=1
            maxF = max(maxF,dic[s[j]])
            if j-left+1 > k+maxF:
                dic[s[left]] -=1
                left +=1
        return len(s)-left