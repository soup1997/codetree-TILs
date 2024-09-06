import sys

n, m, k = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
block = [1] * m
block_range = [k-1, k+m-1]

if n == 1:
    print(1)

else:
    for i in range(1, len(grid)):
        if not all(grid[i][k-1:k+m-1]):
            grid[i][k-1:k+m-1] = block
            break

    for row in grid:
        print(*row)