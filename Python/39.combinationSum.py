class Solution(object):
    def findTarget(self,candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[int]
        """        
        tmp = 0
        rst = []
        numCandi = len(candidates)
        for i in xrange(numCandi):
            # Case 1, target found
            if candidates[i] == target:
                rst.append(candidates[i])
                return rst
            # Case 2, candidates larger than target, pass
            if candidates[i] > target:
                continue
            # Case 3, candidate smaller than the target
            if candidates[i] < target:
                tmp = target - candidates[i]
                resultFound = self.findTarget(candidates[i:numCandi],tmp)
                if len(resultFound) > 0:
                    return [candidates[i]]+resultFound 
        # Program reaches here means no target found in the candidates, thus, return empty list
        return []
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        rst = []
        result = []
        numCandi = len(candidates)
        for i in xrange(numCandi):
            # Case 1, candidate is larger than target
            if candidates[i] > target:
                continue
            # Case 2, candidate is the target
            if candidates[i] == target:
                if [target] not in rst:
                    rst.append([target])
            # Case 3, candidate is smaller than target
            if candidates[i] < target:
                newTarget = target - candidates[i]
                result = self.combinationSum(candidates[i:numCandi],newTarget)
                numRst = len(result)
                if numRst > 0:
                    for j in xrange(numRst):
                        if [candidates[i]] + result[j] not in rst:
                            rst.append([candidates[i]] + result[j])
                            
            #result = self.findTarget(candidates[i:numCandi], target)
            #if len(result) > 0 and result not in rst:
            #    rst.append(result)
            #    result = []
                
        return rst