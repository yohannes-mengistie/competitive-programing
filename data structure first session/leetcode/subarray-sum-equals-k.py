class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        prifx = 0
        hashmap = {0:1}
        for i in nums:
            prifx += i
            if prifx -k in hashmap:
                ans  = ans + hashmap[prifx-k]
            if prifx in hashmap:
                hashmap[prifx] = hashmap[prifx] + 1
            else:
                hashmap[prifx] = 1
        
        return ans

        