class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        lastRow = []
        if rowIndex == 0:
            lastRow.append([1])
            return lastRow

        thisRow = [1] * (rowIndex + 1)
        lastRow = self.getRow(rowIndex-1)
        for i in range(1, rowIndex):
            thisRow[i] = lastRow[i-1] + lastRow[i]       
        return thisRow

print(Solution().getRow(34))