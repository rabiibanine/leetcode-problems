class Solution:
    def smallestIndex(self, nums):
        for i, num in enumerate(nums):
            if i == self.getSumNum(num):
                return i
        return -1

    def getSumNum(self, num):
        sum = 0
        while num / 10 != 0:
            sum += num % 10
            num //= 10
        return sum

    def test(self):
        print(self.smallestIndex([1, 3, 2]))  # Should be 2
        print(self.smallestIndex([1, 10, 11]))  # Should be 2


solution = Solution()

solution.test()
