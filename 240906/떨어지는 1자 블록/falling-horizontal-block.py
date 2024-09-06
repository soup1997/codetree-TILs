import sys

n, m, k = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
block = [1] * m
block_range = [k-1, k+m-1]

if n == 1:
    print(1)

else:
    max_row = 0
    for i in range(len(grid)):
        if grid[i][k-1:k+m-1] == [0] * m:
            max_row = max(max_row, i)

    grid[max_row][k-1:k+m-1] = block

    for row in grid:
        print(*row)