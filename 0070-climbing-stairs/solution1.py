import math


class Solution:
    def climbStairs(self, n: int) -> int:
        ways_to_climb = 0
        for i in range((n // 2) + 1):
            ways_to_climb += math.comb(n - i, i)

        return ways_to_climb

    def test(self):
        print(self.climbStairs(2))
        print(self.climbStairs(3))
        print(self.climbStairs(4))
        print(self.climbStairs(5))
        return 0


solution = Solution()

solution.test()
