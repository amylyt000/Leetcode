class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        '''
        O(n^2)

        max_area = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                min_h = min(height[i], height[j])
                area = min_h * (j-i)

                if area > max_area:
                    max_area = area


        return max_area
        '''
        L, R, width, max_area = 0, len(height)-1, len(height)-1, 0

        for w in range(width, 0, -1):
            if height[L] < height[R]:
                max_area = max(height[L] * w, max_area)
                L += 1
            else:
                max_area = max(height[R] * w, max_area)
                R -= 1

        return max_area

print(Solution().maxArea([2, 3, 4, 5, 18, 17, 6]))

