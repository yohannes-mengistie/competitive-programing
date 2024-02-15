class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = defaultdict(int)
        for letter in s:
            dic[letter] +=1
        ans = 0
        odd_have = False
        for key,val in dic.items():
            if val%2 == 0:
                ans +=val
            else:
                odd_have = True
                ans += (val-1)

        if odd_have:
            return ans +1
        else:
            return ans
