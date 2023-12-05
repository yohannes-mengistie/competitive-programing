class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffle = [0]*len(s)
        for index,indice in enumerate(indices):
            shuffle[indice] = s[index]
            print(shuffle)
        return "".join(shuffle)