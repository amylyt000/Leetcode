class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left = ['(', '{', '[']
        right = [')', '}', ']']

        if len(s) %2 != 0 or s[-1] in left:
            return False
        
        
        i = 0
        first = s[i]
        second = s[i+1]

        while s:
            first = s[i]
            second = s[i+1]

            if first in left and second in right and left.index(first) == right.index(second):
                s = s[:i] + s[i+2:]
                i -= 1
                
            elif second in left :
                i += 1

            else:
                return False

        return True

print(Solution().isValid('{[]}'))

