class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {0: "I", 1: "V", 2: "X", 3: "L", 4: "C", 5: "D", 6: "M"}
        result = ""
        rank = 0
        while num // 10 != 0 or num % 10 != 0:
            digit = num % 10
            num //= 10
            if (digit % 5) <= 3:
                result = (
                    symbols[rank + digit // 5] * (digit // 5)
                    + symbols[rank] * (digit % 5)
                    + result
                )
            else:
                result = symbols[rank] + symbols[rank + (digit // 5) + 1] + result
            rank += 2
        return result

    def test(self):
        print(self.intToRoman(3749))
        print(self.intToRoman(1234))
        print(self.intToRoman(3321))


solution = Solution()

solution.test()
