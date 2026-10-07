class Solution:
    def __init__(self):
        self.results: dict[int, int] = {0: 1, 1: 1}

    def climbStairs(self, n: int) -> int:
        if n not in self.results:
            self.results[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.results[n]

    def test(self):
        print(self.climbStairs(2))
        print(self.climbStairs(3))
        print(self.climbStairs(4))
        print(self.climbStairs(5))
        print(self.climbStairs(8))


solution = Solution()

solution.test()
