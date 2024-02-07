class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0]*(n+1)
        for shift in shifts:
            a,b,c = shift

            if c == 0:
                arr[a] -=1
                arr[b+1] +=1
            else:
                arr[a] +=1
                arr[b+1] -=1

        for i in range(1,n):
            arr[i] += arr[i-1]
        ans = ""
        for j in range(n):
            st = s[j]
            shift = arr[j]
            ch = ord("a") + (ord(st)-ord("a")+shift)%26
            ans += chr(ch)
        return ans

