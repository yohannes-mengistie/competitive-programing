class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        hashmap = {}
        
        for ind in range(len(list1)):
            if list1[ind] in list2:
                hashmap[list1[ind]] = ind + list2.index(list1[ind])
        for value in hashmap.values():
            ans.append(value)
        min_value = min(ans)
        output = []
        for key,value in hashmap.items():
            if value == min_value:
                output.append(key)
        return output

        
            

       