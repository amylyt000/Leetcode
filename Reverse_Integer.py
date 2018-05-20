class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if -10 < x < 10:
            return x
        else:
            newNum = ''

            if x>0:
                sign = +1
            else:
                sign = -1

            x = sign * x
            # print(x)

            while (x//10 != 0):
                x, remain = x//10, x%10
                # print(x, remain)
                if remain == 0 and newNum == '':
                    continue
                else:
                    newNum += str(remain)
                    # print(newNum)

            newNum += str(x)
            # print(newNum)

            newNum = int(newNum)*sign

            if newNum > 2**31 - 1 or newNum < -2**31:
                return 0
            else:
                return newNum

print(Solution().reverse(-321))