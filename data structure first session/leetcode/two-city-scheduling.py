class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        arr = sorted(costs,key = lambda a:a[0]-a[1])
       
        # arr = []
        # dic = {}
        # for i in range(n):
          
        #         dif = costs[i][0]-costs[i][1]
        #         arr.append(dif)

        #         if dif in dic:
        #             dic[dif] = (dic[dif])[0]+costs[i][0]
        #         else:
        #            dic[dif] = costs[i]
        # arr.sort()
        ans = 0
        # print(dic)
        # print(arr)
        for i in range(n):
            if i < n//2:
               ans += arr[i][0]
            else:
                ans+= arr[i][1]
        return ans


