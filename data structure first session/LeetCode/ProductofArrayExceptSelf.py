class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pref =[1]*(n)
        post = [1]*(n)
        for ind in range(1,n):
            pref[ind] = pref[ind-1]*nums[ind-1]
        for j in reversed(range(n-1)):
            post[j] = post[j+1]*nums[j+1]
        l = 0
        while l < len(post):
            pref[l] = pref[l]*post[l]
            l +=1
        return pref