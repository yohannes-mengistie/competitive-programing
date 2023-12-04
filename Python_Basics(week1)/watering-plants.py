class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        ans = 0
        start = capacity
        for i in range(len(plants)):
            if capacity < plants[i]:
                ans = ans+ (i+1)+i
                print(ans)
                capacity = start
                capacity -= plants[i]
            elif capacity >= plants[i]:
                ans +=1
                capacity -= plants[i]
        return ans