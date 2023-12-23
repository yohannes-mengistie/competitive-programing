class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        n  = len(strs[0])
        for i in range(n):
            arr = []
            for j in range(len(strs)):
                if arr and ord(arr[-1]) > ord(strs[j][i]):
                    count +=1
                    break
                arr.append(strs[j][i])

        return count
