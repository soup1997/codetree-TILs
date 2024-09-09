import sys
from collections import deque

n = int(sys.stdin.readline())
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
grid = [[0 for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
directions = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
q = deque()

def inRange(x, y):
    return (0 <= x) and (x < n) and (0 <= y) and (y < n)

def isVisited(x, y):
    return visited[x][y]

def canGo(x, y):
    return inRange(x, y) and not isVisited(x, y)

def bfs():
    sx, sy = r1-1, c1-1

    grid[sx][sy] = 0 # 거리 정보 저장
    visited[sx][sy] = True
    q.append((sx, sy))

    while q:
        nx, ny = q.popleft()

        for direction in directions:
            dx, dy = direction[0], direction[1]
            x, y = nx + dx, ny + dy

            if canGo(x, y):
                grid[x][y] = grid[nx][ny] + 1
                visited[x][y] = True
                q.append((x, y))


ex, ey = r2-1, c2-1
bfs()

if visited[ex][ey]:
    print(grid[ex][ey])

else:
    print(-1)