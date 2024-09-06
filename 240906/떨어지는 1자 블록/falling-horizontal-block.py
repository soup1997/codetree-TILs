import sys

n, m, k = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

block = [1] * m
block_range = [k-1, k+m-1]

max_row = 0

for i in range(len(grid)):
    if grid[i][k-1:k+m-1].count(0) == m:
        max_row = max(max_row, i)
    
    else: # max row를 찾으면서 중간에 블록 막혀있으면 더 이상 탐색할 필요 없음
        break

grid[max_row][k-1:k+m-1] = block

for row in grid:
    print(*row)