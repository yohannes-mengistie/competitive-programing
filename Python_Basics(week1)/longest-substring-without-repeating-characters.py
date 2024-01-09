class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        l = 0
        ma = 0
        for i,v in enumerate(s):
            if v in d and l<=d[v]:
                l = d[v] +1
            else:
                ma = max(ma,i-l+1)
            d[v] = i
        return ma  
                



        