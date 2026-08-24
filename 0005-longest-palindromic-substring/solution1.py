class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_substring = ""
        substring = ""

        for i in range(len(s)):

            # First check (odd)
            j = -1
            while True:
                j += 1
                if i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                    continue
                else:
                    substring = s[i - j + 1 : i + j]
                    break

            # Second check (even)
            j = -1
            while True:
                j += 1
                if i - j >= 0 and i + j + 1 < len(s) and s[i - j] == s[i + j + 1]:
                    continue
                else:
                    if len(s[i - j + 1 : i + j + 1]) > len(substring):
                        substring = s[i - j + 1 : i + j + 1]
                    break

            if len(substring) > len(longest_substring):
                longest_substring = substring

        return longest_substring

    def test(self):
        print(self.longestPalindrome("cbbd"))
        print(self.longestPalindrome("babad"))


solution = Solution()

solution.test()
