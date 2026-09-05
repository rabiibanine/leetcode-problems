class Solution:
    def binary_search(self, lo, hi, array, predicate):
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if predicate(array[mid]):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def find_rotation_point(self, array):
        i = self.binary_search(0, len(array), array, lambda x: x < array[0])
        return i if i < len(array) else -1

    def search(self, nums, target):
        rotation_point = self.find_rotation_point(nums)
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (rotation_point + lo + (hi - lo) // 2) % len(nums)
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        final_index = lo if lo < len(nums) and nums[lo] == target else -1
        return final_index

    def test(self):
        array1 = [4, 5, 6, 7, 0, 1, 2]
        array2 = [4, 5, 6, 7, 8, 0, 2]
        array3 = [3, 1]
        print(self.search(array3, 3), ", expected: 0")
        print(self.search(array1, 1), ", expected: 5")


solution = Solution()


solution.test()
