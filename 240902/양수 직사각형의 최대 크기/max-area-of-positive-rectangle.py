import sys

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def isPositive(x, y):
    return grid[x][y] > 0

def calcSize(x, y):
    square_size = 0

    for i in range(x, n):
        for j in range(y, m):
            if isPositive(i, j):
                square_size += 1
            
            else:
                break
    
    return square_size


if __name__=='__main__':
    sizes = []
    for i in range(n):
        for j in range(m):
            if isPositive(i, j):
                square_size = calcSize(i, j)
                sizes.append(square_size)
    if len(sizes) == 0:
        print(-1)
    
    else:
        print(max(sizes))