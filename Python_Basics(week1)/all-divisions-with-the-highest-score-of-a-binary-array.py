class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
            tot = sum(nums)
            nums = [0]+nums
            dic = {}
            count_0 = 0
            arr = []
            dic[0] = tot
            arr.append(tot)
            for ind in range(1,len(nums)):
                if nums[ind] == 0:
                    count_0 +=1
                    ans = count_0 + tot
                    dic[ind] = ans
                    arr.append(ans)
                
                elif ind == len(nums)-1:
                    ans = count_0
                    dic[ind] = ans
                    arr.append(ans)
                else:
                    ans = tot-nums[ind] + count_0
                    tot -=1
                    dic[ind] = ans
                    arr.append(ans)
            
            ma = max(arr)
            
            output = []
            for key,value in dic.items():
                if value == ma:
                    output.append(key)
            return output
            











        
            



        
