class Solution:
    def largestOddNumber(self, num: str) -> str:
        min_odd = 0
        right = len(num)-1
        while right >= 0:
            if int(num[right])%2!=0:
                return num[:right+1]
            else:
                num = num[:right]
            right -=1
        return ""