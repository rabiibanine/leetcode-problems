# This solution uses string reversing (yes that getIthInteger method is completely useless)
class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0:
            isNegative = True
            x *= -1
        return int(str(x)[::-1]) * (-1 if isNegative else 1)

    def getIthInteger(self, x: int, i: int) -> int:
        return (x // 10**i) % 10

    def test(self):
        print(self.reverse(-1234567))


solution = Solution()

solution.test()
