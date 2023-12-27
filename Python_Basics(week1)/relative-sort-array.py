class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}
        for num in arr1:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] +=1
        res = []
        #temp = list(set(arr1))
        for numm in arr1:
            if numm not in arr2:
                res.append(numm)
        print(res)
        res.sort()
        ans = []
        for val in arr2:
            for j in range(dic[val]):
                ans.append(val)
        return ans+res