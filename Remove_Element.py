class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pos = -1


        for i in range(len(nums)):
        	if nums[i] != val:
        		pos += 1
        		nums[pos] = nums[i]

        return (pos+1)

print(Solution().removeElement([], 2))

