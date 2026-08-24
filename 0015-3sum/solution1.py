from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        three_array = [nums[i], nums[j], nums[k]]
                        three_array.sort()
                        print(three_array)
                        if three_array not in result:
                            result.append(three_array)

        return result

    def test(self):
        arr = [-1, 0, 1, 2, -1, -4]
        print(self.threeSum(arr))


solution = Solution()

solution.test()
