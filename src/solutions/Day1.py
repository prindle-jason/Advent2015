# https://adventofcode.com/2022/day/1
from adventutil.DataImport import InputType
from adventutil.Day import Day
#from adventutil.ListHelper import list_split

YEAR, DAY = 2015, 1

EXPECTED_A = 138
EXPECTED_B = 1771
INPUT_TYPE = InputType.LIVE_DATA

class Day1(Day):
    def __init__(self):
        super().__init__(YEAR, DAY, EXPECTED_A, EXPECTED_B)

    def partA(self):
        line = self.lines[0]
        return line.count('(') - line.count(')')
        #return 2 * line.count('(') - len(line)

    def partB(self):
        line = self.lines[0]
        floor = 0

        for index in range(len(line)):
            floor += 1 if line[index] == '(' else -1
            if floor == -1:
                return index + 1

if __name__ == '__main__':
    Day1().run(INPUT_TYPE)