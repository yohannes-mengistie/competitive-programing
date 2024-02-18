class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if len(palindrome) == 1:
            return ""
        
        ans = ""
        for i in range(n):
            if palindrome[i] != "a":
                ans += "a"
                ans += palindrome[i+1:]
                if ans != ans[::-1]:
                    return ans
                else:
                    break
            ans += palindrome[i]
        
        return palindrome[:-1] + "b"

                

        if ans[-1] == "z":
            ans[-1] = "a"
            return "".join(ans)
        else:
            ans[-1] = chr(ord(ans[-1])+1)
            return "".join(ans)

            

           

