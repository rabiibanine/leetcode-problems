from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        distance = r
        max_area = 0
        area = 0

        while True:
            if height[l] < height[r]:
                area = height[l] * distance
                distance -= 1
                l += 1
            else:
                area = height[r] * distance
                distance -= 1
                r -= 1

            if area > max_area:
                max_area = area

            if r - l <= 0:
                break

        return max_area

    def test(self):
        print(self.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
        print(self.maxArea([8, 7, 2, 1]))


solution = Solution()

solution.test()
