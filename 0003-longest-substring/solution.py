class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        for center in range(n):
            window = {s[center]}
            length = 1
            l = r = 0
            left_blocked = right_blocked = False
            while not (left_blocked and right_blocked):
                if not right_blocked:
                    r += 1
                    idx = center + r
                    if idx < n and s[idx] not in window:
                        window.add(s[idx])
                        length += 1
                    else:
                        right_blocked = True
                if not left_blocked:
                    l += 1
                    idx = center - l
                    if idx >= 0 and s[idx] not in window:
                        window.add(s[idx])
                        length += 1
                    else:
                        left_blocked = True
            longest = max(longest, length)
        return longest

    def test(self):
        print(self.lengthOfLongestSubstring("abcabcd"))
        print(self.lengthOfLongestSubstring("1R1T7"))
        print(self.lengthOfLongestSubstring("abcabcbb"))
        print(self.lengthOfLongestSubstring("S"))
        return 0


solution = Solution()

solution.test()
