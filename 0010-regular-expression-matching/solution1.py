class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(p):

            if j < len(p) - 1 and p[j + 1] == "*":
                char = s[i]
                while i < len(s) and (s[i] == p[j] == char or p[j] == "."):
                    i += 1
                j += 2
                continue
            elif s[i] == p[j]:
                i += 1
                j += 1
                continue
            elif p[j] == ".":
                i += 1
                j += 1
                continue

            return False

        if len(s[i:]) or len(p[j:]):
            return False

        return True

    def test(self):
        # print(self.isMatch("aaa", "aa.*"))
        # print(self.isMatch("aa", "a*"))
        # print(self.isMatch("aab", "c*a*b"))
        print(self.isMatch("mississippi", "mis*is*ip*."))


solution = Solution()

solution.test()
