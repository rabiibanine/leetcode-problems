class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = n >= 0
        product = 1
        curr_pow = 1
        cache = {1: x}

        if n < 0:
            n = -n

        while curr_pow * 2 < n:
            cache[curr_pow * 2] = cache[curr_pow] * cache[curr_pow]
            curr_pow *= 2

        curr_product_pow = 0

        while curr_product_pow < n:
            if curr_pow * curr_product_pow > n:
                curr_pow //= 2
                continue

            product *= cache[curr_pow]
            curr_product_pow += curr_pow

        return product if sign else 1 / product

    def test(self):
        print(self.myPow(3, 0))
        print(self.myPow(3, 1))
        print(self.myPow(3, 2))
        print(self.myPow(3, 3))
        print(self.myPow(3, -3))
        print(self.myPow(3, 24))


solution = Solution()

solution.test()
