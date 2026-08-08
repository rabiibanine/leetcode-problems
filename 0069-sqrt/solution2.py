class Solution:
    def mySqrt(self, x: int) -> int:

        x_bit_length = x.bit_length()
        step = 2 ** (x_bit_length / 2)
        for i in range(4):
            step = self.babylonian(step, x)

        return int(step // 1)

    def babylonian(self, x: float, y: int) -> float:
        return 1 / 2 * (x + y / x)

    def abs(self, x: int) -> int:
        if x < 0:
            return -x
        return x

    def test(self):
        for i in range(200):
            print(f"{i}: {self.mySqrt(i)}")


solution1 = Solution()

solution1.test()
