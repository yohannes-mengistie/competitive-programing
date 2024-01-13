class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        i,r = 0,k-1
        min = len(blocks)
        while r <= len(blocks)-1:
            new = blocks[i:r+1]
            c1 = new.count("W")
            if c1 <= min:
                min =c1
            r +=1
            i +=1
        return min