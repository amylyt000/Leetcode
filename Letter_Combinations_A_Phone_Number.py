class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        num_letter = {}
        num_letter[2] = ('a', 'b', 'c')
        num_letter[3] = ('d', 'e', 'f')
        num_letter[4] = ('g', 'h', 'i')
        num_letter[5] = ('j', 'k', 'l')
        num_letter[6] = ('m', 'n', 'o')
        num_letter[7] = ('p', 'q', 'r', 's')
        num_letter[8] = ('t', 'u', 'v')
        num_letter[9] = ('w', 'x', 'y', 'z')


        # string = []
        digits = str(digits)
        # 23
        string = [""]
        if digits == "":
            return []

        for d in digits:
            tmp = []
            for new in num_letter[int(d)]:
                for old in string:
                    tmp += [old+new]
                # tmp += [old+new for old in string]
            string = tmp

        return string


print(Solution().letterCombinations(""))





