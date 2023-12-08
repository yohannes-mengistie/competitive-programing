class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        temp = "\n".join(source)
        output= ""
        #print(temp)

        i = 0
        while i < len(temp):

            jump = temp[i:i+2]
            if jump == "//":

                i += 2
                while i < len(temp) and temp[i] != "\n":
                    i += 1

            elif jump == "/*":

                i += 2
                while temp[i:i+2] != "*/":
                    i += 1
                i += 2

            else:
                output += temp[i]
                i += 1

        
        ans = []
        #print(output)
        print(output.split("\n"))

        for line in output.split("\n"):
            if line != "":
                ans.append(line)


        return ans