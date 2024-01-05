class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        left = 0 ; right = 0
        ans = []
        while left < len(firstList) and right < len(secondList):
            if firstList[left][0] <= secondList[right][1] and firstList[left][1] >= secondList[right][0]:
                ans.append([max(secondList[right][0],firstList[left][0]),min(firstList[left][1],secondList[right][1])])

            elif firstList[left][1] >= secondList[right][0] and firstList[left][0] <= secondList[right][1]:
                ans.append([max(secondList[right][0],firstList[left][0]),min(firstList[left][1],secondList[right][1])])

            if firstList[left][1] >= secondList[right][1]:
                right +=1
            elif firstList[left][1] <= secondList[right][1]:
                left +=1

            else:
                ans.append([])
                left +=1
                right +=1

        return ans


