class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        nums[queries[0][1]] = queries[0][0] + nums[queries[0][1]]
        ans = 0
        for num in nums:
            if num%2==0:
                ans +=num
        output = [ans]
        for ind in range(1,len(queries)):
            res = nums[queries[ind][1]]
            nums[queries[ind][1]] = queries[ind][0] +  nums[queries[ind][1]]
            if  nums[queries[ind][1]]%2 != 0 and res %2 == 0:
                ans -= res
                output.append(ans)
            elif nums[queries[ind][1]]%2 == 0 and res %2 == 0:
                ans = ans + (nums[queries[ind][1]] - res)
                output.append(ans)
            elif nums[queries[ind][1]]%2 == 0 and res %2 != 0:
                ans += nums[queries[ind][1]] 
                output.append(ans)
            else:
                output.append(ans)
        return output
            


