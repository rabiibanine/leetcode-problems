class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = False
        currentIndex = -1
        string = ""

        largestLength = len(a) if len(a) >= len(b) else len(b)
        for i in range(largestLength):

            bitA = a[currentIndex] if i < len(a) else "0"
            bitB = b[currentIndex] if i < len(b) else "0"

            carryChar = "1" if carry else "0"
            temp = bitA + bitB + carryChar

            match temp.count("1"):
                case 0:
                    string += "0"
                    carry = False
                case 1:
                    string += "1"
                    carry = False
                case 2:
                    string += "0"
                    carry = True
                case 3:
                    string += "1"
                    carry = True

            currentIndex -= 1

        if carry == True:
            string += "1"

        return string[::-1]

    def test(self):
        string1 = "1"
        string2 = "101"
        print(self.addBinary(string1, string2))


solution1 = Solution()

solution1.test()
