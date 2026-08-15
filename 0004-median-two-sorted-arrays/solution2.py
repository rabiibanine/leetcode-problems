from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_array = []
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        i = 0
        j = 0

        # Special cases
        if nums1_len == 0:
            return self.getArrayMedian(nums2)
        if nums2_len == 0:
            return self.getArrayMedian(nums1)

        if nums2_len == 0:
            return self.getArrayMedian(nums1)

        while len(sorted_array) < nums1_len + nums2_len:
            num1 = nums1[i] if i < nums1_len else nums2[-1] + 1
            num2 = nums2[j] if j < nums2_len else nums1[-1] + 1

            if num1 < num2:
                sorted_array.append(num1)
                i += 1
            elif num1 >= num2:
                sorted_array.append(num2)
                j += 1

            print(num1)
            print(num2)
            print(sorted_array)

        return self.getArrayMedian(sorted_array)

    def getArrayMedian(self, nums: List[int]) -> float:
        nums_len = len(nums)

        if nums_len == 0:
            return 0
        if nums_len % 2 == 0:
            return nums[nums_len // 2]
        return (nums[nums_len // 2] + nums[nums_len // 2 - 1]) / 2

    def test(self):
        print(self.findMedianSortedArrays([1, 3, 5], [2, 4, 6, 7]))
        print(self.findMedianSortedArrays([], []))
        print(self.findMedianSortedArrays([], [1, 2, 3]))


solution = Solution()

solution.test()
