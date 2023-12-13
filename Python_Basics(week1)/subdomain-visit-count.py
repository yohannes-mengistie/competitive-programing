class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = {}
        def sub_division(visit,domain):
            if domain in hashmap:
                hashmap[domain] += visit
            else:
                hashmap[domain] = visit
            for ind in range(len(domain)):
                if domain[ind] == ".":
                    sub_division(visit,domain[ind+1:])
                    return
        for cpd in cpdomains:
            cur = cpd.split()
            sub_division(int(cur[0]),cur[1])
        ans = []
        for key,value in hashmap.items():
            ans.append(str(value) + " " + key)
        return ans

