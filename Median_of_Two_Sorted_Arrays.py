class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        nums = []
        for i in range(len1):
            nums.append(nums1[i])
        for i in range(len2):
            nums.append(nums2[i])

        print(nums)
        nums.sort()
        length = len(nums)
        
        if length%2 == 0:
            med = (nums[length//2-1] + nums[length//2])/2
        else:
            med = nums[length//2]
                
        return med
        
nums1 = [1, 2]
nums2 = [3, 4]

med = Solution().findMedianSortedArrays(nums1, nums2)
print(med)