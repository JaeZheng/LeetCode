class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        left = 0
        right = len(height)-1

        while left < right:
            maxArea = max(maxArea, (right-left)*(min(height[left], height[right])))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maxArea

s = Solution()
height = [1,8,6,2,5,4,8,3,7]
a = s.maxArea(height)
print(a)