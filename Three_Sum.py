class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        # print(nums)
        sol = []
        
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]: # to avoid repeatedness
                continue
            l = i+1
            r = len(nums)-1

            while l < r:
                sumNum = nums[i] + nums[l] + nums[r]

                if sumNum < 0:
                    l+=1
                elif sumNum > 0:
                    r-=1
                else:
                    sol.append((nums[i], nums[l], nums[r]))

                    while (l<r) and (nums[l] == nums[l+1]):
                        l+=1

                    while (l<r) and (nums[r] == nums[r-1]):
                        r-=1

                    l+=1
                    r-=1    

        return sol


print(Solution().threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))
# [-5, -5, -4, -4, -4, -2, -2, -2, 0, 0, 0, 1, 1, 3, 4, 4]
