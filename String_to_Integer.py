class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()

        # print(str)
        newStr = ''
        for i in range(len(str)):
            if (str[i] == '-' or str[i] == '+') and newStr == '':
                newStr += str[i]
            elif (str[i] == '-' or str[i] == '+') and newStr != '':
                break
            elif str[i].isdigit():
                newStr += str[i]
            else:
                break
        
        
        # print(newStr)
        if newStr == "" or newStr == "-" or newStr == "+":
            return 0
        
        def del_zero(string):

          
            new_str = ''
            for i in range(len(string)):
                if string[i] != 0:
                    new_str += string[i]
                else:
                    continue

            return int(new_str)


        if newStr[0] == '-':
            sign = -1
            num = sign*int(del_zero(newStr[1:]))
        elif newStr[0] == '+':
            num = int(del_zero(newStr[1:]))
        else:
            num = int(del_zero(newStr))


            
        if num > (2**31-1):
            return 2**31-1
        elif num < -2**31:
            return -2**31
        else:
            return num
                    
print(Solution().myAtoi('+0 123'))                  
print(Solution().myAtoi('+1'))        
print(Solution().myAtoi('42'))
print(Solution().myAtoi("   -42-"))
print(Solution().myAtoi("4193 with words"))
print(Solution().myAtoi("words and 987"))
print(Solution().myAtoi("-91283472332"))


