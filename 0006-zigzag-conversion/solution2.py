class Solution:
    def convert(self, s: str, numRows: int) -> str:
        current_index = 0
        result = ""
        while True:
            if current_index >= len(s):
                break

            result += s[current_index]

            current_index += 4

        return result

    def test(self):
        print(self.convert("PAYPALISHIRING", 3))
        print(self.convert("PAYPALISHIRING", 4))


solution = Solution()

solution.test()
