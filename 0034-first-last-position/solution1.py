class Solution:
    def binary_search(self, lo, hi, array, predicate):
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if predicate(array[mid]):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def find_first(self, target, array):
        i = self.binary_search(0, len(array), array, lambda x: x >= target)
        return i if i < len(array) and array[i] == target else -1

    def find_last(self, target, array):
        i = self.binary_search(0, len(array), array, lambda x: x > target) - 1
        return i if i < len(array) and array[i] == target else -1

    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        return [self.find_first(target, nums), self.find_last(target, nums)]

    def test(self):
        array1 = [1, 2, 2, 2, 3]
        print(self.searchRange(array1, 2))
        print(self.searchRange([], 0))


solution = Solution()

solution.test()
