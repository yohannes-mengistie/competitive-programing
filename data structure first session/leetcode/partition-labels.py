class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        ans,hashmap,max_seen,count = [],{},0,0
        for i , char in enumerate(s):
            hashmap[char] = i
        for i,char in enumerate(s):
            max_seen = max(max_seen,hashmap[char])
            count +=1
            print(max_seen)
            if i == max_seen:
                ans.append(count)
                count = 0
        return ans
        