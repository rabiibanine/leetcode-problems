class Solution:
    def binary_search(self, lo, hi, array, predicate):
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if predicate(array[mid]):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def find_first(self, array, target):
        i = self.binary_search(0, len(array), array, lambda x: x >= target)
        return i if i < len(array) and array[i] == target else -1

    def find_row(self, matrix, target):
        lo = 0
        hi = len(matrix)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if matrix[mid][-1] >= target:
                hi = mid
            else:
                lo = mid + 1
        return lo if lo < len(matrix) else -1

    def searchMatrix(self, matrix, target):
        row_index = self.find_row(matrix, target)
        if row_index < 0:
            return False
        return self.find_first(matrix[row_index], target) >= 0

    def test(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        matrix2 = [[1]]
        print(self.searchMatrix(matrix2, 2))


solution = Solution()

solution.test()
