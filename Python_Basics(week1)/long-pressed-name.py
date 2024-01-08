class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
           index1 = 0
           index2 = 0

           while index1 <= len(name) and index2 < len(typed):
               if index1 < len(name) and name[index1] == typed[index2]:
                   index1 +=1
                   index2 +=1
               elif index1 != 0 and name[index1-1] == typed[index2]:
                   index2 +=1


               else:
                    return False
           return index1 == len(name) and index2 == len(typed)
                