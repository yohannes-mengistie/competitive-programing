class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr = []
        cur = set(spaces)
        for i,v in enumerate(s):
            if i in cur:
                arr.append(" ")
            arr.append(v)
                
        return "".join(arr)