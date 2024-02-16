class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        print(path)
        for i in range(len(path)):
            if path[i] == ".." :
                if len(stack) >= 1:
                   stack.pop()
            elif path[i] and path[i] != ".":
                stack.append(path[i])

        return "/"+"/".join(stack)