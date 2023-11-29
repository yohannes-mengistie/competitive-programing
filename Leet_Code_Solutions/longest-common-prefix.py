class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        res = []
        for j in strs:
            res.append(len(j))
        n = min(res)

        for i in range(n):
            letter = strs[0][i]
            for j in strs:
                if j[i] != letter:
                    return ans
            ans += letter
        return ans
        