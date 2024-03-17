class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters)-1
        ans = ""
        while low <= high:
            mid = (low+high)//2
            if letters[mid]<= target:
                low = mid+1
            elif letters[mid] > target:
                ans = letters[mid]
                high = mid-1
        if not ans:
            return letters[0]
        return ans
                