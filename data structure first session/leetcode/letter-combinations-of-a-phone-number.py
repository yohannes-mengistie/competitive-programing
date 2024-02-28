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
        if not digits :
            return []
        output = ['']
        for i in digits:
            res = []
            for j in sample[i]:
                for k in output:
                    res.append(k+j)
            output = res
        return output