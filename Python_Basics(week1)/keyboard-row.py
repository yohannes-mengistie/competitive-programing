class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        
        row2 = "asdfghjkl"
        
        row3 = "zxcvbnm"
        
        ans = []
        for word in words:
            temp = word.lower()
            if len(set(temp+row1))==len(row1) or len(set(temp+row2)) == len(row2)or len(set(temp+row3))==len(row3):
                ans.append(word)
            
        return ans

