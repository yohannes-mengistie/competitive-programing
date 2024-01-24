class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
           nums1.sort()
           nums2.sort()
           ans = []
           l = 0 ; r = 0
           while l<len(nums1) and r  < len(nums2):
               if  nums1[l] > nums2[r]:
                   r +=1
               elif nums1[l] < nums2[r]:
                   l +=1

               else:
                   ans.append(nums1[l])
                   l +=1
                   r +=1

           return ans