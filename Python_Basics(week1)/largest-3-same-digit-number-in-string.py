class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = []
        output = ""
        l = 0 ; r=2
        while r<len(num):
            if len(set(num[l:r+1])) == 1:
                ans.append(num[l:r+1])
            r +=1
            l +=1
        ans.sort()
        if ans:
            return ans[-1]
        else:
            return output