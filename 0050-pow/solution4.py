class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1 / x, -n
        result = 1.0
        while n:
            if n & 1:  # this bit of n is set: include the current x^(2^k)
                result *= x
            x *= x  # x becomes x^(2^(k+1))
            n >>= 1
        return result
