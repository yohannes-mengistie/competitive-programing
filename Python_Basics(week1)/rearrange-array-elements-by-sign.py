class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nega_num = []
        pose_num = []
        for num in nums:
            if num < 0:
                nega_num.append(num)
            else:
                pose_num.append(num)
        l=0;r=0
        ans = []
        while l < len( nega_num ) and r<len(pose_num):
            ans.append(pose_num[l])
            ans.append(nega_num[r])
            l +=1
            r +=1
        return ans

