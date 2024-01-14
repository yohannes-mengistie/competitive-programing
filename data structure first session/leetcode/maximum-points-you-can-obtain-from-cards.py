class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = len(cardPoints) - k

        tot = sum(cardPoints[right:])
        score = tot

        while right<len(cardPoints):

            tot += (cardPoints[left] - cardPoints[right])
            score = max(score,tot)
            left += 1
            right += 1
        
        return score