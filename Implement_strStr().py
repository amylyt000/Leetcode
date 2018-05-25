class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if not needle:
            return 0


        if len(haystack) < len(needle):
            return -1


        for i in range(len(haystack)-len(needle)+1):
            flag = True
            # print("i", i)
            if haystack[i] == needle[0]:
                pos = i
                for j in range(len(needle)):
                    # print("j", j)
                    if needle[j] != haystack[pos+j]:
                        flag = False
                        # break
                if flag == True:
                    return pos

        return -1

print(Solution().strStr("mississippi", "issip"))

# for i in range(5):
#   for j in range(5):
#       print(i,j)
#       if j == 3:
#           break
# indicates "break" just break the innermost iteration


'''
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.index(needle) if needle in haystack else -1
'''