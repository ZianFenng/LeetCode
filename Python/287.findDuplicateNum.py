# O(nlgn) solution to this problem
# Binary search is used here
# the for loop scan through the array every time
# mid, low, high are numbers in 1 ~ n, not any indexes of the array nums
# the basic idea is that since we know that there is duplicate and
# the duplicate is only of one number
# say duplicate is a, b < a, c > a, a,b and c are all within the range of [1, n]
# then, number of i in nums less than b won't be larger than b
# number of i in nums less than c should be larger than c

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums) - 1
        
        while low < high:
            
            mid = (high-low)/2 + low 
            
            count = 0
            
            for i in nums:
                if i <= mid:
                    count += 1
            
            if count > mid:
                high = int(mid)
            else:
                low = int(mid + 1)
        
        return low
