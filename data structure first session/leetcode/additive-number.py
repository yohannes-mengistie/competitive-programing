class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        s=num
        current = []
        def backtrack(idx):
            print(current)
            if idx >= len(s):
                return len(current) >= 3

            for i in range(idx,len(s)):
                val = s[idx:i+1]
                if len(val) > 1 and val[0] == "0":
                    return False

                if len(current)<=1 or int(val) == current[-1]+current[-2]:
                    current.append(int(val)) 
                    if backtrack(i+1):
                        return True
                    current.pop()

                # elif len(current) <= 1:
                #     current.append(val) 
                #     if backtrack(i+1):
                #         return True
                #     current.pop()
                    
            return False
        return backtrack(0)