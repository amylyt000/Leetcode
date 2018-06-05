class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 0:
            return []
        result = [[1]]
        for i in range(1, numRows):
            print(i)
            result.append([1]*(i+1))
            for j in range(1, i):
                print(result[i-1][j-1])
                print(result[i-1][j])

                result[i][j] = result[i-1][j-1] + result[i-1][j]
        
        return result

print(Solution().generate(3))