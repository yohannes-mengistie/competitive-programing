class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left = 0
        s = list(s)
        print(s)
        while left < len(s):
            s[left:left+k] = s[left:left+k][::-1]
            left += k*2
        return "".join(s)
