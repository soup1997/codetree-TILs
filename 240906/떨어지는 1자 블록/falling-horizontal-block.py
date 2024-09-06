import sys

n, m, k = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
block = [1] * m
block_range = [k-1, k+m-1]


for i in range(len(grid)):
    if any(grid[i][k-1:k+m-1]):
        grid[i-1][k-1:k+m-1] = block
        break

for row in grid:
    print(*row)