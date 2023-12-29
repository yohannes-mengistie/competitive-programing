class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s.split())
        n = len(s)
        arr = [0]*n
        
        for val in  s:
            cur = int(val[-1])
            arr[cur-1] = val[:-1]

        return " ".join(arr)

        