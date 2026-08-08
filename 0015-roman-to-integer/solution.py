class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        sum = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s):
                if roman_dictionary[s[i + 1]] > roman_dictionary[s[i]]:
                    sum += roman_dictionary[s[i + 1]] - roman_dictionary[s[i]]
                    i += 2
                    continue
            sum += roman_dictionary[s[i]]
            i += 1

        return sum

    def test(self):
        print(self.romanToInt("IV"))
        print(self.romanToInt("LVIII"))
        print(self.romanToInt("MCMXCIV"))


solution = Solution()

solution.test()
