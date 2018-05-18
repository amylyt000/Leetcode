class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        import numpy as np
        s = '#' + '#'.join(s) + '#'
        RL = [0] * len(s)
        maxLen = 0
        pos = 0
        maxRight = 0

        for i in range(len(s)):
            if i < maxRight:
                RL[i] = min(RL[2*pos - i], maxRight - i)
            else:
                RL[i] = 1

            while (i-RL[i]) >= 0 and (i+RL[i])<len(s) and s[i-RL[i]] == s[i+RL[i]]:
                RL[i] += 1

            if i+RL[i]-1 > maxRight:
                maxRight = i+RL[i]-1
                pos = i

            # maxLen = max(maxLen, RL[i]-1)
        center = np.argmax(RL)
        longest = s[center-RL[center]+1:center+RL[center]]
        longest = longest[1:-1]
        

        return longest[::2]

longest = Solution().longestPalindrome('abcdcab')
print(longest)





