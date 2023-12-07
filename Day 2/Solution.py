from collections import defaultdict


class Solution:

    def __init__(self):
        self.startingHand = {'green': 13, 'red': 12, 'blue': 14}

    def calculateSolutions(self, fileName):
        file = open(fileName)
        result = 0
        powerSetResult = 0

        for line in file.read().split('\n'):

            # replace annoying stuff
            line = line.replace(",", "")
            line = line.replace(";", "")
            line = line.replace(":", "")

            items = line.split(" ")

            id = int(items[1])

            hashmap = defaultdict(int)

            for i in range(2, len(items) - 1, 2):

                color = items[i + 1]
                count = items[i]
                hashmap[color] = max(hashmap[color], int(count))

            result += id
            for key in self.startingHand.keys():

                if hashmap[key] > self.startingHand[key]:
                    result -= id
                    break


            power = 1
            for value in hashmap.values():
                power *= value
            powerSetResult += power


        print(result)
        print(powerSetResult)


sol = Solution()
sol.calculateSolutions("input.txt")