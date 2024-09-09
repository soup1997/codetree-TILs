import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(m) for _ in range(n)]
visited = [[[False, 0] for _ in range(m)] for _ in range(n)] # 방문 여부와 시작점으로 부터 거리 동시 저장
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
q = deque()

def inRange(x, y):
    return (0 <= x) and (x < n) and (0 <= y) and (y < m)

def isVisited(x, y): # 방문 여부 확인
    return visited[x][y][0]

def snake(x, y):
    return grid[x][y] == 0

def canGo(x, y):
    return inRange(x, y) and not isVisited(x, y) and not snake(x, y)

def bfs():
    sx, sy = 0, 0

    visited[sx][sy][0] = True
    visited[sx][sy][1] = 0
    q.append([sx, sy, 0]) # 시작점 위치와 거리 정보 추가

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