class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans=0
        hashmap =defaultdict()
        stack=[]
        i,j=0,0

        while j<len(fruits):
            if fruits[j] not in hashmap and len(hashmap)<2:
                stack.append(fruits[j])
                hashmap[fruits[j]]=j
                j+=1

            elif  fruits[j] in hashmap:
                hashmap[fruits[j]]=j
                j+=1

            else:  
                if hashmap[stack[0]]>hashmap[stack[1]]  :
                    i = hashmap[stack[1]]+1
                    del hashmap[stack[1]]
                    stack.pop()
                else:
                    i = hashmap[stack[0]]+1
                    del hashmap[stack[0]] 
                    stack.pop(0)              
            
            ans=max(ans,j-i)
        return ans