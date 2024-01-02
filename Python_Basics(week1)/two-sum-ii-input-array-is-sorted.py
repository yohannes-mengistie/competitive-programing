class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 ; right = len(numbers)-1
        ans = []
        while left < right:
            cur = numbers[left]+numbers[right]
            if cur < target:
                left +=1

            elif cur > target:
                right -=1

            else:
                ans.append(left+1)
                ans.append(right+1)
                left +=1
                right -=1

        return ans
