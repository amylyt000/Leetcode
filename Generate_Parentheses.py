class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
       

        def addOn(n):
            if n == 1:
                return ["()"]
            else:
                last = set(addOn(n-1))
        
                new = set()
                for i in last:
                    for j in range(len(i)):
                
                        tmp = i[:j]+"()"+i[j:]
                        # if tmp not in new:
                        new.add(tmp)
                        
                return list(new)

        return addOn(n)

print(Solution().generateParenthesis(3))



# set can make sure there is no repetition, then don't need to check if tmp not in new