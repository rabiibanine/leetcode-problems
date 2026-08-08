from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        first = nums[0]
        last = nums[-1]

        result = []
        for i in range(first + 1, last):
            present = False
            for num in nums:
                if num == i:
                    present = True
                    break
            if not present:
                result.append(i)

        return result

    def test(self):
        array = [1, 2, 10]
        print(self.findMissingElements(array))


solution = Solution()

solution.test()
