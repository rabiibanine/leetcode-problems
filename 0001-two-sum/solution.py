from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            index_i = nums.index(i)
            for j in nums[index_i:]:
                if i + j == target:
                    return [i, j]
        return [0, 0]

    def test(self):
        array = [2, 7, 11, 15]
        print(self.twoSum(array, 9))


solution1 = Solution()

solution1.test()
