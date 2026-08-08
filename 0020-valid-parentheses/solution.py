class Solution:
    def isValid(self, s: str) -> bool:
        open = {"(", "{", "["}
        close = {")", "}", "]"}
        parenth_dict = {"(": 1, ")": 1, "{": 2, "}": 2, "[": 3, "]": 3}
        array = []

        for char in s:
            if char in open:
                array.append(char)
            if char in close:
                if len(array) == 0:
                    return False
                if parenth_dict[char] != parenth_dict[array[-1]]:
                    return False
                else:
                    array.pop()
        if len(array) > 0:
            return False
        return True

    def test(self):
        print(self.isValid("(){()}[]"))
        print(self.isValid("(){()}[)]"))
        print(self.isValid("]"))
        print(self.isValid("["))


solution = Solution()

solution.test()
