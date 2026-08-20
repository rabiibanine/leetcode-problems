from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        # We're searching over the shorter array, switch arrays if nums1 is longer than nums2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l = 0
        r = len(nums1)
        num_elems = (len(nums1) + len(nums2) + 1) // 2
        while l < r:
            mid = l + (r - l) // 2
            # Comparing nums1[i] with nums2[j - 1]
            outside = nums1[mid]
            inside = (
                nums2[num_elems - mid - 1]
                if num_elems - mid - 1 < len(nums2)
                else nums1[-1] + 1
            )
            if inside <= outside:
                r = mid
            else:
                l = mid + 1

        # Calculating the median
        j = num_elems - l
        if bool(nums1[l - 1 : l]) and bool(nums2[j - 1 : j]):
            num1 = max(nums1[l - 1], nums2[j - 1])
        else:
            num1 = max(
                nums1[l - 1] if nums1[l - 1 : l] else float("-inf"),
                nums2[j - 1] if nums2[j - 1 : j] else float("-inf"),
            )

        if bool(nums1[l : l + 1]) and bool(nums2[j : j + 1]):
            num2 = min(nums1[l], nums2[j])
        else:
            num2 = min(
                nums1[l] if nums1[l : l + 1] else float("+inf"),
                nums2[j] if nums2[j : j + 1] else float("+inf"),
            )

        median = (num1 + num2) / 2 if not (total_length % 2 == 0) else num1

        return median

    def test(self):
        arr = [1, 3, 5, 7, 9]
        arr2 = [2, 4, 6, 8, 10]
        arr3 = [1, 2, 3, 4, 5]
        arr4 = [6, 7, 8, 9]
        arr5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        arr6 = [1, 1, 2, 3, 3, 3, 6, 7, 8, 9]

        # print(self.findMedianSortedArrays(arr, arr2))
        print(self.findMedianSortedArrays(arr3, arr4))


solution = Solution()

solution.test()
