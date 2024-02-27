class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(oc,cc,cur):
            if oc==cc== n:
                result.append("".join(cur))
                return
            if oc <n:
                cur.append("(")
                dfs(oc+1,cc,cur)
                cur.pop()
            if cc < oc:
                cur.append(")")
                dfs(oc,cc+1,cur)
                cur.pop()
        dfs(0,0,[])
        return result
            