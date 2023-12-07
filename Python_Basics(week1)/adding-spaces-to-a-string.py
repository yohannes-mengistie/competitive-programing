class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        arr = []
        cur = set(spaces)
        for i,v in enumerate(s):
            if i in cur:
                arr.append(" ")
            arr.append(v)
                
        return "".join(arr)