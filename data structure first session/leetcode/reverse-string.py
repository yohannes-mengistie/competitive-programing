class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverseA(s,st,end):
            if st >= end:
                return 
            else:
                s[st],s[end] = s[end],s[st]
                return reverseA(s,st+1,end-1)
        return reverseA(s,0,len(s)-1)
    

