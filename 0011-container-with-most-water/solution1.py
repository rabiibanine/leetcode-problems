from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        height_len = len(height)
        for i in range(height_len):
            h1 = height[i]
            for j in range(i + 1, height_len):
                h2 = height[j]
                distance = j - i
                area = min(h1, h2) * distance
                if area > max_area:
                    max_area = area

        return max_area

    def test(self):
        print(self.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
        print(self.maxArea([1, 1]))


solution = Solution()

solution.test()
