class Solution:
    def findKthLargest(self, nums, k):
        largest = 0

        for i in range(k):
            largest = self.popLargest(nums)

        return largest

    def popLargest(self, array):
        largest_index = 0
        for i in range(1, len(array)):
            if array[largest_index] < array[i]:
                largest_index = i
        return array.pop(largest_index)

    def test(self):
        print(self.findKthLargest([1, 2, 3], 1))
        print(self.findKthLargest([1, 2, 3], 2))
        print(self.findKthLargest([1, 2, 3], 3))


solution = Solution()

solution.test()
