# class Solution:
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         low = 0
#         high = len(nums)-1
#         # while low <= high:
#         while low < len(nums) and nums[low] < target:
#             low += 1
#         while high >= 0 and nums[high] > target:
#             high -= 1

#         if low <= high:
#             return [low, high]
#         else:
#             return [-1, -1]

# print(Solution().searchRange([5,7,7,8,8,10], 6))

class Solution:
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1, -1]
        else:
            low = nums.index(target)
            high = len(nums) - 1 - nums[::-1].index(target)
            return [low, high]


print(Solution().searchRange([5,7,7,8,8,10], 8))

