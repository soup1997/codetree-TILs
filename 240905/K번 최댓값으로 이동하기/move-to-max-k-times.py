# 우선순위(숫자, -행, -열)

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
grid = [(list(map(int, sys.stdin.readline().split()))) for _ in range(n)]
r, c = map(int, sys.stdin.readline().split())
r, c = r-1, c-1
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

sx, sy = r, c # 시작 기준 좌표

def inRange(x, y): 
    return (0 <= x) and (x < n) and (0 <= y) and (y < n)

def canGo(x, y, ref):
    return inRange(x, y) and not visited[x][y] and grid[x][y] < ref

# Repeat BFS k times
for _ in range(k):
    maxval = 0
    visited = [[False for _ in range(n)] for _ in range(n)]

    # bfs 시작
    q = deque()
    q.append((sx, sy)) # 기준 좌표 넣고 시작
    visited[sx][sy] = True # 기준 좌표 방문 처리

    while q:
        x, y = q.popleft()

        for direction in directions:
            dx, dy = direction[0], direction[1]
            X, Y = x + dx, y + dy

            if canGo(X, Y, grid[r][c]): # 우선순위 1: 현재 기준좌표보다 작은 값이어야 함
                q.append((X, Y))
                visited[X][Y] = True

                # maxval 업데이트용 
                if grid[X][Y] > maxval:
                    maxval = grid[X][Y]
                    sx, sy = X, Y

                elif grid[X][Y] == maxval: # 현재 탐색 값이 maxval과 같은 값이라면
                    if X < sx or (X >= sx and Y < sy): # 우선순위 2 거나 우선순위 3인지 확인
                        sx, sy = X, Y
    
    r, c = sx, sy # 다음 시작점 최종 업데이트

print(f'{sx+1} {sy+1}')