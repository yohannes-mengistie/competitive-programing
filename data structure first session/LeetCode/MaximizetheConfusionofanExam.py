class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        d ={"T":0 ,"F":0}
        i = 0
        maxF = 0
        for j in range(len(answerKey)):
            d[answerKey[j]] +=1
            maxF = max(maxF,d[answerKey[j]])
            if j-i+1 > k+maxF:
                d[answerKey[i]] -=1
                i +=1
        return len(answerKey)-i