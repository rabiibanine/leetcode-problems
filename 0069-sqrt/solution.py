class Solution:
    def mySqrt(self, x: int) -> int:

        current_number = 0
        while current_number * current_number <= x:
            current_number += 1
        return current_number - 1

    def abs(self, x: int) -> int:
        if x < 0:
            return -x
        return x

    def test(self):
        for i in range(200):
            print(f"{i}: {self.mySqrt(i)}")


solution1 = Solution()

solution1.test()
