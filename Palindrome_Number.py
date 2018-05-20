class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        if 0 <= x < 10:
            return True

        ranger = 10
        while x//ranger >= 10:
            ranger *= 10

        print(ranger)

        while x:
            print(x)
           
            left = x//ranger
            right = x%10
            print(left, right)
            if left != right:
                return False

            # x = (x%ranger)//10
            if x>10:
                x = (x - left*ranger - right)//10
            else:
                return True
            # print(x)

            ranger /= 100

        return True


print(Solution().isPalindrome(100021))








