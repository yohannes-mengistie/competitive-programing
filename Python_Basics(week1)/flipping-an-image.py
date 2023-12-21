class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            l = 0
            r = len(image)-1
            while l<=r:
                if image[i][l] == image[i][r]:
                    image[i][r] = int(not(image[i][r]))
                    image[i][l] = image[i][r]

                l +=1
                r -=1
        return image