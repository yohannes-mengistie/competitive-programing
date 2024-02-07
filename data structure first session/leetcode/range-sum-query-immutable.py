class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        for ind in range(1,len(nums)):
            self.arr[ind] +=self.arr[ind-1] 

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.arr[right]
        else:
            return self.arr[right] - self.arr[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)