from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j = 0

        while len(strs) > 1 and len(strs[0]) > 0 and strs[0][:j] == strs[1][:j]:
            j += 1

        for i in range(2, len(strs)):
            while strs[0][:j] != strs[i][:j]:
                j -= 1

        return strs[0][:j]

    def test(self):
        # print(self.longestCommonPrefix(["dog", "racecar", "car"]))
        print(self.longestCommonPrefix(["", ""]))
        print(self.longestCommonPrefix([""]))
        print(self.longestCommonPrefix(["flower", "flow", "flight"]))


solution = Solution()

solution.test()
