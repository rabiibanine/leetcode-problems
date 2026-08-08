class Solution:
    # TODO Fix this
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest_length = 0
        current_length = 0

        # Trivial cases
        if s == "":
            return 0

        if s[1:2] == "":
            return 1

        while True:

            # Increase the window from the right
            r += 1

            # If we meet a duplicate character step from the left
            if s[l] == s[r]:
                l += 1

            # Set the current_length to whatever the length of the string
            # in the window is
            current_length = r - l + 1

            if current_length > longest_length:
                longest_length = current_length

            if r + 1 >= len(s):
                break

        return longest_length

    def test(self):
        print(self.lengthOfLongestSubstring("S"))
        print(self.lengthOfLongestSubstring("abacd"))
        print(self.lengthOfLongestSubstring(""))


solution = Solution()

solution.test()
