'''
Largest Island Area (a.k.a. “Max Area of Island”)

Problem:
Given a 2D grid where:

1 = land

0 = water

Return the maximum area (number of cells) of any single island. If there are no islands, return 0.

1 1 0 0
1 0 1 1
0 0 1 1

Islands:

top-left island area = 3

bottom-right island area = 3
So output = 3
'''

def largest_island_area(grid):
    if not grid or not grid[0]:
        return 0 
    
    rows, cols = len(grid), len(grid[0])
    max_area = 0

    def dfs(r,c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 0
        
        grid[r][c] = 0 # Mark as visited
        area = 1
        area += dfs(r+1, c)
        area += dfs(r-1, c)
        area += dfs(r, c+1)
        area += dfs(r, c-1)

        return area 
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r,c))
    
    return max_area


# example
grid = [
    [1, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 0, 1, 1]
]

print(largest_island_area(grid))