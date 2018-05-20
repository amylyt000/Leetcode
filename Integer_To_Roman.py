class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str

        1. break the number to each digit
        2. see whether this is number is 4, 9, 40, 90, 400, 900
        """
        roman = ""
		

        keys = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        dic = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

        cur_id = -1
        while num:
        	while num >= keys[cur_id]:
        		roman += dic[cur_id]
        		num -= keys[cur_id]
        	cur_id -= 1

        return roman

print(Solution().intToRoman(1994))









        