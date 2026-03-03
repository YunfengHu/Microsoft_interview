'''
Question: Number of Islands (Microsoft Classic)
Problem

You are given a 2D grid:

'1' = land

'0' = water

An island is formed by connecting adjacent lands horizontally or vertically (4-direction).

Return the total number of islands.

grid =
1 1 0 0
1 0 0 1
0 0 1 0

Output: 3
'''

from typing import List 

def numIslands(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0 
    
    rows, cols = len(grid), len(grid[0])
    islands = 0 

    def dfs(r:int, c:int):
        if r<0 or r>=rows or c<0 or c>=cols or grid[r][c] == '0':
            return
        
        grid[r][c] = '0' # Mark as visited

        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(r,c)
                
    return islands


# example   
grid = [
    ['1', '1', '0', '0'],
    ['1', '0', '0', '1'],
    ['0', '0', '1', '0']
]

print(numIslands(grid))