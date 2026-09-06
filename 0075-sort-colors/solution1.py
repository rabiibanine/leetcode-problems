class Solution:
    def sortColors(self, nums):
        sorted = False
        while not sorted:
            sorted = True
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[j] < nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
                        sorted = False

    def test(self):
        array1 = [2, 0, 2, 1, 1, 0]
        self.sortColors(array1)
        print(array1)


solution = Solution()

solution.test()
