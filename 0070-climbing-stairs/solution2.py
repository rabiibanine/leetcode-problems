class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def test(self):
        print(self.climbStairs(2))
        print(self.climbStairs(3))
        print(self.climbStairs(4))
        print(self.climbStairs(5))
        print(self.climbStairs(8))


solution = Solution()

solution.test()
