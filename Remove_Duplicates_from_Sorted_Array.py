class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        for i in range(1, len(nums)):
            if nums[i] != nums[pos]:
                pos += 1
                nums[pos] = nums[i]

        return (pos+1)

print(Solution().removeDuplicates([1]))

