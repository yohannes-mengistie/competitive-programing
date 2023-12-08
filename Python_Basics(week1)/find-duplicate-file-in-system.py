class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = []
        hashmap = {}
        
        for path in paths:
            path = path.split()
            directry_path = path[0]
            for filee in path[1:]:
                first = filee.index("(")
                last = filee.index(")")
                check = filee[first+1 : last]
                if check not in hashmap:
                    hashmap[check] = [directry_path +"/" + filee[:first] ]
                else:
                    hashmap[check].append(directry_path +"/" + filee[:first])

        for key,value in hashmap.items():
            if len(value) > 1:
                ans.append(value)

        return ans