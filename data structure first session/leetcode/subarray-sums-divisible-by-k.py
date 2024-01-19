from collections import Counter
class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashmap = {0:1}
        count=ans =0
        res = 0
        for i in nums:
            res +=i
            if res%k in hashmap:
                ans = ans + hashmap[res%k]
                hashmap[res%k] = hashmap[res%k] + 1
            else:
                hashmap[res%k] =1

        return ans
        




        
            

        