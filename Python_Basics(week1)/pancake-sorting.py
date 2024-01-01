class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        output = []
        for i in range(n):
            max_val = max(arr[:n-i])
            val_ind = arr.index(max_val)+1
            arr[:val_ind] = reversed(arr[:val_ind])
            output.append(val_ind)
            arr[:max_val] = reversed(arr[:max_val])
            output.append(max_val)
        return output