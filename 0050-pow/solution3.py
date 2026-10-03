class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = n >= 0
        n = n if sign else -n
        if n == 0:
            return 1
        else:
            result = 0
            if n % 2 == 0:
                result = self.myPow(x * x, n // 2)
            else:
                result = self.myPow(x * x, n // 2) * x
            return result if sign else 1 / result

    def test(self):
        print(self.myPow(2, -1025))


solution = Solution()

solution.test()
