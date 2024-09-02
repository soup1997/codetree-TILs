import sys
sys.setrecursionlimit(100000)

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def isSquare(sx, sy, ex, ey):
    for i in range(sx, ex):
        for j in range(sy, ey):
            if grid[i][j] < 0:
                return False
    
    return True

def maxSquare(x, y)
    square_size = -1

    for i in range(x, n):
        for j in range(y, m):
            if isSquare(x, y, i, j):
                size = (i - (x+1)) * (j - (y+1))
                square_size = max(square_size, size)
    
    return square_size


max_size = -1

for i in range(n):
    for j in range(m):
        max_size = max(max_size, maxSquare(i, j))

print(max_size)