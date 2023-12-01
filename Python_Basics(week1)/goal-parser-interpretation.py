class Solution:
    def interpret(self, command: str) -> str:
        
        l = 0 ; r=1
        ans = []
        while r < len(command)+1:
            if command[l] == '(' and command[r] == ')':
                ans.append('o')
            elif command[l].isalnum():
                ans.append(command[l])
            elif command[l].isalnum():
                ans.append(command[r])
            l +=1 ; r +=1
        return "".join(ans)
            
                
            
