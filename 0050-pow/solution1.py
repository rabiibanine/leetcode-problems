class Solution:
    def myPow(self, x: float, n: int) -> float:
        product = 1
        if n >= 0:
            for i in range(n):
                product *= x
        else:
            for i in range(-n):
                product /= x

        return product

    def test(self):
        print(self.myPow(2, 4))
        print(self.myPow(-2, 3))
        print(self.myPow(2, -2))


solution = Solution()

solution.test()
