class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        for token in tokens:
            if len(stack) > 1 and token =="+":
                a = stack.pop()
                b = stack .pop()
                ans = int(b)+int(a)
                stack.append(ans)
            
            elif len(stack) > 1 and token =="-":
                a = stack.pop()
                b = stack .pop()
                ans = int(b)-int(a)
                stack.append(ans)
            elif len(stack) > 1 and token =="*":
                a = stack.pop()
                b = stack .pop()
                ans = int(b)*int(a)
                stack.append(ans)
            elif len(stack) > 1 and token =="/":
                a = stack.pop()
                b = stack.pop()
               
                ans = int(int(b)/int(a))
                stack.append(ans)
            
            else:
                stack.append(token)
           

        return int(stack[-1])