from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(x) for x in str(int("".join([str(x) for x in digits])) + 1)]

    def test(self):
        array = [9, 9]
        print(self.plusOne(array))


solution1 = Solution()

solution1.test()
