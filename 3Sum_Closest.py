class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import numpy as np
        diff = np.inf
        nums.sort() #[-4, -4, -4, -1, 0, 1, 2]

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1

            while l < r:
                sumNum = nums[i] + nums[l] + nums[r]
                if abs(sumNum - target) < diff:
                    diff, sol = abs(sumNum - target), sumNum

                if sumNum < target:
                    l += 1

                elif sumNum > target:
                    r -= 1

                else:
                    return sol                      
                

        return sol


print(Solution().threeSumClosest([1, 1, 1, 0], -100))



