import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(m) for _ in range(n)]
visited = [[[False, 0] for _ in range(m)] for _ in range(n)]
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
q = deque()

def inRange(x, y):
    return (0 <= x) and (x < n) and (0 <= y) and (y < n)

def isVisited(x, y):
    return visited[x][y][0]

def snake(x, y):
    return grid[x][y] == 0

def canGo(x, y):
    return inRange(x, y) and not isVisited(x, y) and not snake(x, y)

def bfs():
    sx, sy, dist = 0, 0, 0

    visited[sx][sy][0] = True
    visited[sx][sy][1] = dist
    q.append([sx, sy, dist])

    while q:
        nx, ny, dist = q.popleft()

        for direction in directions:
            dx, dy = direction[0], direction[1]
            x, y = nx + dx, ny + dy

            if canGo(x, y):
                q.append([x, y, dist + 1])
                visited[x][y][0] = True
                visited[x][y][1] = dist + 1

bfs()
if visited[-1][-1][0]:
    print(visited[-1][-1][1])

else:
    print(-1)