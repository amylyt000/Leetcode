class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
        	return s

        step, zigzag = numRows + (numRows - 2), ''

        for i in range(numRows):
        	for j in range(i, len(s), step):
        		zigzag += s[j]
        		if i!= 0 and i!= (numRows-1) and (j-i+2*(numRows-1)-i) < len(s):
        			zigzag += s[j-i+2*(numRows-1)-i]

        return zigzag

zigzag = Solution().convert('PAYPALISHIRING', 4)
print(zigzag)


