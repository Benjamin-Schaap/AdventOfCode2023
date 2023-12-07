# lol part two was nasty
class Solution:

    def __init__(self):
        self.calibrationValues = []

    def loadInput(self, fileName):
        file = open(fileName)

        for line in file.read().split('\n'):

            left = 0
            right = len(line) - 1

            result = 0

            while not line[left].isdigit():
                left += 1
            
            result = int(line[left]) * 10

            while not line[right].isdigit():
                right -= 1

            result += int(line[right])

            print(result, line)
            self.calibrationValues.append(result)

        print(self.calibrationValues)

    def compute(self):
        print(sum(self.calibrationValues))

sol = Solution()
sol.loadInput("input.txt")
sol.compute()