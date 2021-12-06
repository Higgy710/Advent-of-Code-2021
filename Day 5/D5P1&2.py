# -*- coding: utf-8 -*-
"""
--- Day 5: Hydrothermal Venture ---

You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2

Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

    An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
    An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....

In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

"""

class Board():

    def __init__(self):
        self.field = [[0]]
        self.max = [0,0]
        self.marked = 0


    def add(self, start, end, partOne):
        self.adjustField(start, end)
        if start[0] == end[0] or start[1] == end[1]:
            self.markNoneDiagonalFields(start, end)
        elif not partOne:
            self.markDiagonalFields(start,end)


    def adjustField(self, start, end):
        old_x, old_y = self.max[0], self.max[1]

        x_max = start[0] if start[0] > end[0] else end[0]
        if x_max > self.max[0]: self.max[0] = x_max
        self.processDiffs(old_x, 0)

        y_max = start[1] if start[1] > end[1] else end[1]
        if y_max > self.max[1]: self.max[1] = y_max
        self.processDiffs(old_y, 1)



    def processDiffs(self, old, dim):
        if dim == 0:
            for i in range(old+1, self.max[0]+1):
                self.field.append([0])
        else:
            for i in range(self.max[0] + 1):
                self.field[i].extend([0] * (self.max[1]-len(self.field[i])+1))


    def markNoneDiagonalFields(self, start, end):
        x_start, x_end = (start[0], end[0]+1) if start[0] < end[0] else (end[0], start[0]+1)
        y_start, y_end = (start[1], end[1]+1) if start[1] < end[1] else (end[1], start[1]+1)
        for i in range(x_start, x_end):
            for j in range(y_start, y_end):
                self.field[i][j] += 1
                if self.field[i][j] == 2: self.marked += 1

    def markDiagonalFields(self, start, end):
        increase_x = start[0] < end[0]
        increase_y = start[1] < end[1]

        x,y = start[0], start[1]
        self.field[x][y] += 1
        if self.field[x][y] == 2: self.marked += 1

        while x != end[0] and y != end[1]:
            x = x+1 if increase_x else x-1
            y = y+1 if increase_y else y-1
            self.field[x][y] += 1
            if self.field[x][y] == 2: self.marked += 1


with open('input.txt') as f:
    lines = f.readlines()

board_one = Board()
board_two = Board()
for line in lines:
    coordinates = [[int(x) for x in coordinate] for coordinate in [x.split(",") for x in line.split("->")]]
    board_one.add(coordinates[0], coordinates[1], True)
    board_two.add(coordinates[0], coordinates[1], False)

print("Answer 1: %d" %board_one.marked)
print("Answer 2: %d" %board_two.marked)
