# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 15:43:42 2021

@author: danza
"""

def check_neighbors(lp, grid, checked_points):
    i,j = lp[0], lp[1]
    checked_points.append(lp)

    if grid[lp[0]][lp[1]] < 9: sum = 1
    else: return 0

    if i-1 >= 0 and [i-1,j] not in checked_points: sum += check_neighbors([i-1, j], grid, checked_points)
    if i+1 < len(grid)-1 and [i+1,j] not in checked_points: sum += check_neighbors([i+1, j], grid, checked_points)
    if j-1 >= 0 and [i,j-1] not in checked_points: sum += check_neighbors([i, j-1], grid, checked_points)
    if j+1 < len(grid[0])-1 and [i,j+1] not in checked_points: sum += check_neighbors([i, j+1], grid, checked_points)

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
print("Solution part one: %d" %sum_part_one)
print("Solution part two: %d" %product_part_two)
