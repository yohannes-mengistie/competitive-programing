class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dic = {}
        for ind in range(len(nums)):
            if nums[ind] in dic:
                dic[nums[ind]].append(ind)

            else:
                dic[nums[ind]] = [ind]
            

        for key , value in dic.items():
            if len(value) > 1:
                prefix = [0]*len(value)
                tot = 0
                for i in range(len(value)):
                    tot += value[i]
                    prefix[i] = tot

                postfix = [0]*len(value)
                tot = 0
                for i in range(len(value)-1,-1,-1):
                    tot += value[i]
                    postfix[i] =  tot

                for j in range(len(value)):
                    if j == 0:
                        nums[value[j]] = postfix[j+1] - value[j]*(len(value)-j-1)
                    elif j == len(value)-1:
                        nums[value[j]] = value[j]*(j) - prefix[j-1]
                    else:
                        nums[value[j]] = (value[j]*(j) - prefix[j-1]) +  (postfix[j+1] - value[j]*(len(value)-j-1))

            if len(value) == 1:
                nums[value[0]] = 0


        return nums

