class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [i, seen[target - nums[i]]]
            else:
                seen[nums[i]] = i

    def test(self):
        array = [2, 7, 11, 15]
        print(self.twoSum(array, 9))


solution = Solution()

solution.test()
