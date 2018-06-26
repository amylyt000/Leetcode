class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = '1'
        # current = string

        for i in range(1, n):
            count = 1
            current = string
            new = ''
            for j in range(len(current)-1):
                if current[j] == current[j+1]:
                    count += 1
                    # print(count)
                else:
                    new += str(count) + current[j]
                    count = 1
            new += str(count) + current[-1]
            string = new

        return string                
                
                
s = Solution()
print(s.countAndSay(6))

            
            
# 1211
# 111221
# 312211


