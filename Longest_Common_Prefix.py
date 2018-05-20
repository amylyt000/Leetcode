class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
    
        flag = True
        out = ""
        min_len = min(len(str) for str in strs) if len(strs)!= 0 else 0
        
        for i in range(min_len):
            letter = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != letter:
                    flag = False
                    return out
                    # break
            if flag == True:
                out += letter
        return out

                    
                
            
                    
                    
                    
        