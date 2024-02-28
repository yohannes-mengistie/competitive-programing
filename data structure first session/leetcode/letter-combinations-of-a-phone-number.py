class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        sample = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz',
        }
        ans = []
        path = []
        if not digits:
            return ans
        def combination(idx):
            if  idx >= len(digits):
                ans.append("".join(path))
                return
           
            for j in sample[digits[idx]]:
                path.append(j)

                combination(idx+1)
                path.pop()
    

        combination(0)
        return ans        
                