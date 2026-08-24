class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "$" + "#".join(s) + "$"
        radius_arr = [0]
        c = 0
        final_index = 0

        for i in range(1, len(t) - 1):

            # Is there a valid i_mirror
            if i < c + radius_arr[c]:
                i_mirror = 2 * c - i
                seed = radius_arr[i_mirror]
            else:
                seed = 0

            # Save the radius at the current index
            palindrome_length = len(self.expand(i + seed, i + seed, t))
            palindrome_radius = palindrome_length // 2

            # Save the index if the current palindrome has the biggest radius
            if radius_arr[final_index] < palindrome_radius:
                final_index = i

            radius_arr.append(palindrome_radius)

            # Replace center if the palindrome at the current index reaches furthest to the right
            if c + radius_arr[c] < i:
                c = i

        # Transform back and return the substring
        start = (final_index - radius_arr[final_index]) // 2
        length = radius_arr[final_index]
        return s[start : start + length]

    def expand(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]

    def test(self):
        print(self.longestPalindrome("abaad"))


solution = Solution()

solution.test()
