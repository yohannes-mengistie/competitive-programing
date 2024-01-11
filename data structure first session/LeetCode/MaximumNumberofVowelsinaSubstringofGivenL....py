class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0 
        vowel = "a,e,o,i,u"
        count = 0
        max_num = 0
        for i in range(len(s)):
            if s[i] in vowel:
                count +=1
            while i-left >= k:
                if s[left] in vowel:
                    count -=1
                left +=1
            max_num = max(max_num,count)
        return max_num