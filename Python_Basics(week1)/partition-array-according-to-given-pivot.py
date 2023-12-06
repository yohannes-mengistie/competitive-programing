class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        larger = []
        cur  = []
        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                cur.append(num)
            else:
                larger.append(num)
        ans = smaller + cur + larger
        return ans