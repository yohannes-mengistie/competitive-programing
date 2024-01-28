class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        left = 0
        for i in range(len(s2)):
            while i-left+1 == len(s1):
                if sorted(s2[left:i+1]) == s1:
                    return True

                left +=1

        return False
