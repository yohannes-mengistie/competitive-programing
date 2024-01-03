class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0 ; right = len(skill)-1
        tot = 0
        
        while left < right:
            if skill[left]+skill[right] == skill[left+1] + skill[right-1]:
                
                tot += skill[left]*skill[right]

            else:
                return -1

            left +=1
            right -=1

        return tot
