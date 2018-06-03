class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        
        pos = m+n-1
        i = m-1
        j = n-1

        while i != -1 and j != -1:
            a, b = nums1[i], nums2[j]
            if a > b:
                nums1[pos] = a
                i -= 1
                pos -= 1
            elif a < b:
                nums1[pos] = b
                j -= 1
                pos -= 1
            else:
                nums1[pos] = a
                nums1[pos-1] = b
                i -= 1
                j -= 1
                pos -= 2
        
        if i == -1:
            for k in range(j+1):
                nums1[k] = nums2[k]
        
    
                
                
                
                
    