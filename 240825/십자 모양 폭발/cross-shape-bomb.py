import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
r, c = map(int, sys.stdin.readline().split())

r, c = r-1, c-1
size = (arr[r][c]) - 1

# explosion
for i in range(max(0, r-size), min(n, r+1+size)):
    for j in range(max(0, c-size), min(n, c+1+size)):       
        if j > n-1:
            break

        if j == c or i == r:
            arr[i][j] = 0 

# arrangement
for row in range(n-1, 0, -1):
    for col in range(n):
        if arr[row][col] == 0:
            arr[row][col] = arr[row-1][col]
            arr[row-1][col] = 0

for vec in arr:
    print(*vec)