class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output = []
        for arr in points:
            dis = arr[0]**2 + arr[1]**2
            output.append([dis,arr])



        output.sort()
        ans = []
        for i in range(k):
            ans.append(output[i][1])

        return ans
            

            


