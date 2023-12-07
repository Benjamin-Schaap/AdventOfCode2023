from collections import defaultdict


class Solution:

    def __init__(self):
        self.copies = defaultdict(int)
        self.totalscrathcards = 0

    def getSolutions(self, fileName):
        file = open(fileName)
        result = 0

        for line in file.read().split('\n'):

            line = line.replace(":", "")
            items = line.split(" ")
            # remove empty strings
            items = [item for item in items if item]

            winningNums = set()
            handNums = set()
            isWinningNums = True

            # sort out if I'm looking at a winning number, or one I hold. Add to respective lists
            for i in range(2, len(items)):

                if items[i] == "|":
                    isWinningNums = False
                    continue

                if isWinningNums:
                    winningNums.add(int(items[i]))
                else:
                    handNums.add(int(items[i]))
            
            # find out what winning numbers I had
            winners = winningNums.intersection(handNums)

            # if I did win anything, get duplicate tickets based on how many winning
            # numbers I had
            for i in range(len(winners)):

                currentGame = int(items[1])
                nextCards = currentGame + 1

                self.copies[nextCards + i] += 1 + self.copies[currentGame]

            # how many times did I win this card? Count duplicates plus the original
            self.totalscrathcards += 1 + self.copies[int(items[1])]

            # early exits to make the value calculation easier
            if len(winners) == 0:
                continue

            if len(winners) == 1:
                result += 1
                continue

            value = 1

            for _ in range(len(winners) - 1):
                value *= 2

            result += value

            
        print(self.totalscrathcards)


            


sol = Solution()
sol.getSolutions("input.txt")