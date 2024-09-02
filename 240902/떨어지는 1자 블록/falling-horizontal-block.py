import sys

n, m, k = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
block = [1] * m
k = k-1

def fallingDown(k):
    max_row, max_column = 0, k + m-1
    for i in range(1, n):
        for j in range(k, k+m):
            if grid[i][j] == 0:
                max_row = max(max_row, i)
                max_column = max(max_column, j)
            else:
                break

    return max_row, max_column

max_row, max_column = fallingDown(k)
grid[max_row][k:max_column+1] = block

for row in grid:
    print(*row)