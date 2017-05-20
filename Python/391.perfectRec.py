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

    def calArea(self, rectangle):
        """
        :type rectangle: List[int]
        :rtype: int
        """
        longitude = rectangle[2] - rectangle[0]
        latitude  = rectangle[3] - rectangle[1]
        area = longitude * latitude
        return area

    def addRec(self, perfectRec, newRec, L, B):
        """
        :type perfectRec:   List[List[int]]
        :type newRec:       List[int]
        :type L:            int
        :type B:            int
        :rtype:             bool
        """
        width = newRec[2] - newRec[0]
        height = newRec[3] - newRec[1]
        
        startHori  = newRec[0] - L
        startVerti = newRec[1] - B
        
        for i in range(startHori, startHori + width):
            for j in range(startVerti, startVerti + height):
                if perfectRec[j][i]:
                    return False # overlapped
                else:
                    perfectRec[j][i] = True
                    
        return True # Non overlapping

    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # [left, bottom, right , up]
        # Possible perfect rec
        maxRec = self.findMaxCoordinate(rectangles)
        
        # width and height of possible perfect rec
        width = maxRec[2] - maxRec[0]
        height  = maxRec[3] - maxRec[1]
        maxArea = width * height
        
        # Coordinate of the origin of the perfect rec
        originL = maxRec[0]
        originB = maxRec[1]
        
        # Matrix to check overlapping. 0 -> nothing yet,  1 -> occupied
        pfctRec = [ [False]*width for i in range(height) ]        
        numRec = len(rectangles)
        
        allArea = 0
        for i in range(numRec):
            curRec = rectangles[i]
            allArea += self.calArea(curRec)
            if not self.addRec(pfctRec, curRec, originL, originB):
                return False # overlapped, so not perfect rec
       
        if allArea == maxArea:
            return True
        else:
            return False
