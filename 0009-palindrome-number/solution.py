class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x_length = self.getDecimalLength(x)

        for i in range((x_length // 2) + 1):
            if self.getIthDigit(x, i) != self.getIthDigit(x, x_length - 1 - i):
                return False

        return True

    def getDecimalLength(self, x: int) -> int:
        temp = x
        n = 0
        while temp > 0:
            temp = temp // 10
            n += 1
        return n

    def getIthDigit(self, x: int, i: int) -> int:
        return (x // 10**i) % 10  # 0-indexed

    def test(self):
        print(self.isPalindrome(1000001))


solution = Solution()

solution.test()
