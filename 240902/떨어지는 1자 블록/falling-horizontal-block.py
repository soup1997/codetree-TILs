import sys

n, m, k = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

block = [1] * m
k = k-1

def fallingDown(k):
    max_row = 0

    for i in range(n):
        result = any(grid[i][k:k+m]) # 해당 열에서 블록 크기 만큼 슬라이싱했을때 하나라도 1이면 True, 하강 불가
        
        if result: # 모두다 0이라면 블록 하강 가능
            max_row = max(max_row, i-1)
            break

    return max_row

max_row, max_column = fallingDown(k), k + m - 1
grid[max_row][k:max_column+1] = block

for row in grid:
    print(*row)