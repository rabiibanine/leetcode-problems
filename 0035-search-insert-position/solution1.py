class Solution:
    def binary_search(self, lo, hi, array, predicate):
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if predicate(array[mid]):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def find_insert(self, target, array):
        i = self.binary_search(0, len(array), array, lambda x: x >= target)
        return i

    def searchInsert(self, nums, target):
        return self.find_insert(target, nums)

    def test(self):
        array1 = [1, 3, 5, 6]
        print(self.searchInsert(array1, 2))
        print(self.searchInsert(array1, 5))
        print(self.searchInsert(array1, 8))


solution = Solution()

solution.test()
