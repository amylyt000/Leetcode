class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        keys = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        dic = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']


        int_list = []
        for i in range(len(s)):
            id = dic.index(s[i])
            int_list.append(keys[id])
        # print(int_list)

        for i in range(len(int_list)-1):
            if int_list[i] < int_list[i+1]:
                int_list[i] = -int_list[i]

        return sum(int_list)


print(Solution().romanToInt("MCMXCIV"))

