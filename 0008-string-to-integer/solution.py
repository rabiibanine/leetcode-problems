class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        result = 0

        # Step 1
        while s and s[0] == " ":
            s = s[1:]

        # Empty string case
        if s == "":
            return 0

        # Step 2
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        # Step 3
        while s and s[0].isdigit():
            result = result * 10 + int(s[0])
            s = s[1:]
        result *= sign

        # Step 4
        if result > 2**31 - 1:
            return 2**31 - 1
        elif result < -(2**31):
            return -(2**31)
        else:
            return result

    def test(self):
        print(self.myAtoi(" -042"))
        print(self.myAtoi("1337c0d3"))
        print(self.myAtoi(""))
        print(self.myAtoi(" "))
        print(self.myAtoi("+1"))


solution = Solution()

solution.test()
