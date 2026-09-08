class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [0, 0]

    def test(self):
        array = [2, 7, 11, 15]
        print(self.twoSum(array, 9))


solution = Solution()

solution.test()
