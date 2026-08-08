class Solution:
    def convert(self, s: str, numRows: int) -> str:
        forward = True
        zigzag = []

        for i in range(numRows):
            zigzag.append("")

        current_row = 0  # Rows are 0-indexed

        for char in s:

            zigzag[current_row] += char

            if current_row >= numRows - 1:
                forward = False
            elif current_row <= 0:
                forward = True

            current_row += 1 if forward else -1

        return "".join(zigzag)

    def test(self):
        print(self.convert("PAYPALISHIRING", 3))
        print(self.convert("PAYPALISHIRING", 4))
        print(self.convert("A", 4))


solution = Solution()

solution.test()
