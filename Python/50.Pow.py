class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -n
            x = 1/x
        
        result = 1
        while n > 0:
            if n % 2 == 0:
                x = x * x
                n = n / 2
            else:
                n = n - 1
                result = result * x
                n = n / 2
                x = x * x
        return result
        
        # Below also work, just more slow for recursion
        if n == 0:
            return 1
        if n == 1:
            return x
        else:
            if n % 2 == 0:
                return self.myPow(x*x,n/2)
            else:
                n = n - 1
                return x * self.myPow(x*x,n/2)
