class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hashmap = {}

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                res = i+j
                if res not in hashmap:
                    hashmap[res] = [mat[i][j]]
                else:
                    hashmap[res].append(mat[i][j])
        ans = []
        for key, value in hashmap.items():
            length = len(value)
            if key%2!=0:
                for num in value:
                    ans.append(num)
            elif key%2==0:
                value = value[::-1]
                for num in value:
                    ans.append(num)
        return ans