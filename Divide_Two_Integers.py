class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        def within_range(result):
        	if result > 2**31 -1:
        		return 2**31-1
    		elif result < -2**31:
    			return -2*831
    		else:
    			return result

        result = dividend//divisor
        if result < 0:
        	if dividend%divisor == 0:
        		return within_range(result)
        	else:
	        	return within_range(result + 1)
        else:
        	return within_range(result)