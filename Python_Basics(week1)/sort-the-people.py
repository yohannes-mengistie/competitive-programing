class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap = {}
        for ind in range(len(names)):
            hashmap[heights[ind]] = names[ind]
        for i in range(len(names)):
            for j in range(len(names)-1):
                if heights[j] < heights[j+1]:
                    heights[j],heights[j+1] = heights[j+1],heights[j]
        print(heights)
        ans = []
        for value in heights:
            ans.append(hashmap[value])
        
        return ans