'''
Problem Statement

Given a grid of 0s and 1s:

0 = land

1 = water

A closed island is land completely surrounded by water (not touching the boundary).

Return how many closed islands exist.


1 1 1 1 1 1 1
1 0 0 0 0 1 1
1 0 1 1 0 1 1
1 0 0 0 0 1 1
1 1 1 1 1 1 1

Output: 1

Because the land in the middle is fully enclosed.
'''

from typing import List 

def closed_island(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0 
    
    rows, cols = len(grid), len(grid[0])

    def flood(r:int, c:int) -> None:
        stack = [(r,c)]
        grid[r][c] = 1

        while stack:
            x,y = stack.pop()
            for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                nx, ny = x+dx, y+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    stack.append((nx, ny))
    
    # Flood fill from boundaries to mark non-closed islands
    for r in range(rows):
        if grid[r][0] == 0:
            flood(r,0)
        if grid[r][cols-1]==0:
            flood(r, cols -1)
    
    for c in range(cols):
        if grid[0][c] == 0:
            flood(0,c)
        if grid[rows-1][c] == 0:
            flood(rows -1, c)

    # Count closed islands
    count = 0
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == 0:
                count += 1
                flood(r,c)
    
    return count 


# Example usage
grid = [
    [1,1,1,1,1,1,1],
    [1,0,0,0,0,1,1],
    [1,1,1,1,1,1,1],
    [1,0,0,0,0,1,1],
    [1,1,1,1,1,1,1]
]

print(closed_island(grid))  # Output: 1


