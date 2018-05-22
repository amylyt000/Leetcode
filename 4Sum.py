class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        d = {}
        for i in range(len(nums)):
        	for j in range(i+1, len(nums)):
        		sumNum = nums[i] + nums[j]
        		if sumNum in d:
        			d[sumNum].append((i, j))
        		else:
        			d[sumNum] = [(i, j)]
        # print(d)

        sol = []
        for key in d:
        	res = target - key
        	if res in d:
        		list1 = d[res]
        		list2 = d[key]
        		for (i, j) in list1:
        			for (k, l) in list2:
        				if i!= k and i!= l and j!= k and j!= l:
        					tmp = [nums[i], nums[j], nums[k], nums[l]]
        					tmp.sort()
        					if tmp not in sol:
	        					sol.append(tmp)
        return sol

print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))


