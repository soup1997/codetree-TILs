import sys

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

n, m = 4, 5
grid = [[6, -2, 4, -3, 1],
[3, 6, 7, -4, 1],
[6, 1, 8, 15, -5],
[3, -5, 1, 16, 3]]

visited = [[False for _ in range(m)] for _ in range(n)]
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
square_size = 1

def inRange(x, y):
    return (0 <= x) and (x < n) and (0 <= y) and (y < m)

def notVisited(x, y):
    return not visited[x][y]

def isPositive(x, y):
    return grid[x][y] > 0

def canGo(x, y):
    return inRange(x, y) and notVisited(x, y) and isPositive(x, y)

def dfs(x, y):
    global square_size

    visited[x][y] = True

    for direction in directions:
        dx, dy = direction[0], direction[1]
        X, Y = x + dx, y + dy

        if canGo(X, Y):
            visited[X][Y] = True
            square_size += 1
            dfs(X, Y)

if __name__=='__main__':
    sizes = []
    for i in range(n):
        for j in range(m):
            if canGo(i, j):
                dfs(i, j)
                sizes.append(square_size)
                square_size = 1

    if len(sizes) == 0:
        print(-1)
    
    else:
        print(max(sizes))