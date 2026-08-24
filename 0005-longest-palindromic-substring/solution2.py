class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_substring = ""
        substring = ""

        for i in range(len(s)):

            substring_odd = self.expand(i, i, s)
            substring_even = self.expand(i, i + 1, s)
            substring = (
                substring_odd
                if len(substring_even) < len(substring_odd)
                else substring_even
            )

            if len(substring) > len(longest_substring):
                longest_substring = substring

        return longest_substring

    def expand(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]

    def test(self):
        print(self.longestPalindrome("cbbd"))
        print(self.longestPalindrome("babad"))


solution = Solution()

solution.test()
