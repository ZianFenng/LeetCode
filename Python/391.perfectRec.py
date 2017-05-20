class Solution(object):
    def findMaxCoordinate(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: List[int]
        """
        # Record the 'maximum' for the four coordinates
        maxCor = rectangles[0][:]
        # Number of rectangles
        numRec = len(rectangles)
        # Search for the maximum
        for i in range(1,numRec):
            curRec = rectangles[i]# current rectangle
            # Left
            if curRec[0] < maxCor[0]:
                maxCor[0] = curRec[0]
            # Bottom
            if curRec[1] < maxCor[1]:
                maxCor[1] = curRec[1]
            # Right
            if curRec[2] > maxCor[2]:
                maxCor[2] = curRec[2]
            # Up
            if curRec[3] > maxCor[3]:
                maxCor[3] = curRec[3]
        return maxCor
        
    def isAllOverlapping(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        numRec = len(rectangles)
        for i in range(0,numRec-1):
            recI = rectangles[i]
            for j in range(i+1,numRec):
                recJ = rectangles[j]
                if self.isTwoOverlapping(recI, recJ):
                    return True
        return False
                    
    def isTwoOverlapping(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # Condition for non-overlapping
        # if ((rec1[2] <= rec2[0] or rec1[3] <= rec2[1]) or (rec2[2] <= rec1[0] or rec2[3] <= rec1[1])):
            # return False
        # else:
            # return True
        # Condition for overlapping
        # if (rec1[2] > rec2[0] and rec1[3] > rec2[1]) or (rec2[2] > rec1[0] and rec2[3] > rec1[1]):
        #     return True
        # else:
        #     return False
        # if rec1[3] > rec2[1]:
        #     if rec1[1] >= rec2[3]:
        #         return False
        #     elif rec1[2] <= rec2[0] or rec2[2] <= rec1[0]:
        #         return False
        #     else:
        #         return True
        # else:
        #     return False
        
        # if 1.left >= 2.right or 2.left >= 1.right or 1.bottom >= 2.up or 2.bottom >= 1.up
        if (rec1[0] >= rec2[2] or rec2[0] >= rec1[2] or rec1[1] >= rec2[3] or rec2[1] >= rec1[3]):
            return False
        else:
            return True
    
    def calArea(self, rectangle):
        """
        :type rectangle: List[int]
        :rtype: int
        """
        longitude = rectangle[2] - rectangle[0]
        latitude  = rectangle[3] - rectangle[1]
        area = longitude * latitude
        return area
        
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # [left, bottom, right , up]
        numRec = len(rectangles)
        if self.isAllOverlapping(rectangles):
            return False
        else:
            maxRec = self.findMaxCoordinate(rectangles)
            maxArea = self.calArea(maxRec)
            allRecArea = 0
            for i in range(0, numRec):
                curRec = rectangles[i]
                allRecArea += self.calArea(curRec)
            if maxArea == allRecArea:
                return True
            else:
                return False
