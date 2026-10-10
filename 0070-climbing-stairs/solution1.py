import math


class Solution:
    def climbStairs(self, n: int) -> int:
        ways_to_climb = 0
        for i in range(n // 2):
            ways_to_climb += math.factorial(n - i) // math.factorial(n - 2 * i)

        return ways_to_climb

    def test(self):
        print(self.climbStairs(2))
        print(self.climbStairs(3))
        print(self.climbStairs(4))
        print(self.climbStairs(5))


solution = Solution()

solution.test()
