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

    def find_first(self, target, array):
        i = self.binary_search(0, len(array), array, lambda x: x >= target)
        return i if i < len(array) and array[i] == target else -1

    def search(self, nums, target):
        rotation_point = self.find_rotation_point(nums)
        new_array = nums[rotation_point:] + nums[:rotation_point]
        target_index = self.find_first(target, new_array)
        if target_index == -1:
            return -1
        final_index = (rotation_point + target_index) % len(nums)
        return final_index

    def test(self):
        array1 = [4, 5, 6, 7, 0, 1, 2]
        array2 = [4, 5, 6, 7, 8, 0, 2]
        array3 = [3, 1]
        print(self.search(array3, 3))


solution = Solution()


solution.test()
