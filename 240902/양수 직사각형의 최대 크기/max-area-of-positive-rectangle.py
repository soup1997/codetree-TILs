import sys
sys.setrecursionlimit(10000000)

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
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
    
    print(max(-1, max(sizes)))