# Inverting mathematically by walking through the number
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0
        while x:
            result = result * 10 + x % 10
            x //= 10
        return result * sign if not result > 2**31 - 1 else 0

    def test(self):
        print(self.reverse(-123))
        print(self.reverse(1534236469))


solution = Solution()

solution.test()
