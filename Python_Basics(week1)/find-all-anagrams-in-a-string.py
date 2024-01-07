class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic1 = Counter(p)
        dic2 = {}
        n = len(s)
        k = len(p)
        ans = []
        for i in range(n):
            if s[i] in dic2:
                dic2[s[i]] +=1
            else:
                dic2[s[i]] = 1

            if i >= k-1:
                if self.comp(dic1,dic2):
                    ans.append(i-k+1)
                dic2[s[i-k+1]] -=1
        return ans



    def comp(self,dic1,dic2):
        for j in dic1:
            if not(j in dic2 and dic1[j] == dic2[j]):
                return False

        return True