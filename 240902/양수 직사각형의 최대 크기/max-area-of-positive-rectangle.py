import sys
sys.setrecursionlimit(100000)

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def inRange(x, y):
    return 0 <= x < n and 0 <= y < m

def canGo(x, y):
    return inRange(x, y) and not visited[x][y] and grid[x][y] > 0

def dfs(x, y):
    visited[x][y] = True
    min_x, max_x = x, x
    min_y, max_y = y, y

    for dx, dy in directions:
        X, Y = x + dx, y + dy

        if canGo(X, Y):
            visited[X][Y] = True
            sub_min_x, sub_max_x, sub_min_y, sub_max_y = dfs(X, Y)
            min_x, max_x = min(min_x, sub_min_x), max(max_x, sub_max_x)
            min_y, max_y = min(min_y, sub_min_y), max(max_y, sub_max_y)

    return min_x, max_x, min_y, max_y

if __name__ == '__main__':
    max_area = 0

    for i in range(n):
        for j in range(m):
            if canGo(i, j):
                min_x, max_x, min_y, max_y = dfs(i, j)
                area = (max_x - min_x + 1) * (max_y - min_y + 1)
                max_area = max(max_area, area)
    
    print(max_area)