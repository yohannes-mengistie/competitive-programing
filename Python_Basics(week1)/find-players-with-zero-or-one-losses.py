class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winer_dict = {}
        loser_dict = {}
        for x,y in matches:
            if y not in loser_dict:
                loser_dict[y] = 1
            elif y in loser_dict:
                loser_dict[y] +=1
        output1 = []
        output2 = []
        for key,value in loser_dict.items():
            if value < 2:
                output1.append(key)
        for x,y in matches:
            if x not in loser_dict and x not in output2:
                output2.append(x)
        output1.sort()
        output2.sort()
        ans = []
        ans.append(output2)
        ans.append(output1)
        return ans

                