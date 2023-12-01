class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lef =0 ; rig = 0
        cont = max(len(word1),len(word2))
        ans = []
        while cont >0:
            if lef < len(word1):
               ans.append(word1[lef])
            if rig < len(word2):
               ans.append(word2[rig])
            lef +=1
            rig +=1
            cont -=1
        return "".join(ans)
            