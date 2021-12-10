"""
--- Day 9: Smoke Basin ---

These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678

Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

--- Part Two ---

Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678

The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678

The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678

The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678

Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?

"""

def check_neighbors(lp, grid, checked_points):
    i,j = lp[0], lp[1]
    checked_points.append(lp)

    if grid[lp[0]][lp[1]] < 9:
        sum = 1
    else:
        return 0

    if i-1 >= 0 and [i-1,j] not in checked_points:
        sum += check_neighbors([i-1, j], grid, checked_points)
    if i+1 < len(grid)-1 and [i+1,j] not in checked_points:
        sum += check_neighbors([i+1, j], grid, checked_points)
    if j-1 >= 0 and [i,j-1] not in checked_points:
        sum += check_neighbors([i, j-1], grid, checked_points)
    if j+1 < len(grid[0])-1 and [i,j+1] not in checked_points:
        sum += check_neighbors([i, j+1], grid, checked_points)
    return sum


def partOne():
    with open('input.txt') as f:
        lines = f.readlines()

    grid = [[int(line[i]) for i in range(len(line.strip()))] for line in lines]
    sum_of_risk = 0
    low_points = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            bigger_neighbors, neighbors_checked = 0, 0
            if j != 0:
                bigger_neighbors += int(grid[i][j-1] > grid[i][j])
                neighbors_checked += 1
            if j != len(grid[0])-1:
                bigger_neighbors += int(grid[i][j+1] > grid[i][j])
                neighbors_checked += 1
            if i != 0:
                bigger_neighbors += int(grid[i-1][j] > grid[i][j])
                neighbors_checked += 1
            if i != len(grid)-1:
                bigger_neighbors += int(grid[i+1][j] > grid[i][j])
                neighbors_checked += 1
            if neighbors_checked == bigger_neighbors:
                sum_of_risk += 1 + grid[i][j]
                low_points.append([i,j])
    basins = []
    for low_point in low_points:
        basins.append(check_neighbors(low_point, grid,[]))
    basins.sort(reverse=True)
    product_part_two = basins[0] * basins[1] * basins[2]
    return sum_of_risk, product_part_two


sum_part_one, product_part_two = partOne()
print("Solution one: %d" %sum_part_one)
print("Solution two: %d" %product_part_two)
