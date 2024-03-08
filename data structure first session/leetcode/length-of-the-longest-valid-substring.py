class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        maxLen = 0
        forbidden = set(forbidden)
        left = 0
        for i in range(1,len(word)+1):
            for j in range(1,11):
                if i-j < left:
                    break
                if word[i-j:i] in forbidden:
                    left = i-j+1
                    break
            maxLen = max(maxLen,i-left)
        return maxLen
