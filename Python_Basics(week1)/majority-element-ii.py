class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        n = len(nums)
        temp = n//3
        print(temp)
        output = []
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] +=1
        for key,value in hashmap.items():
            if value > temp:
                output.append(key)
        return output
        