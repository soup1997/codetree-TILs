# 조건 1: k번 만큼 반복하며 bfs를 수행해야 함
# 조건 2: 기록해 둔 시작 위치의 값보다 작은 값 중에 제일 큰 값과 그 좌표를 갱신해야함
# 조건 3: 제일 큰 값을 가진 좌표가 여러개일 경우 먼저 행이 작은 순서대로 고려하고 그 다음 열이 작은 순서대로 고려해서 시작점을 갱신해야함

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
grid = [(list(map(int, sys.stdin.readline().split()))) for _ in range(n)]
r, c = map(int, sys.stdin.readline().split())
r, c = r-1, c-1
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

sx, sy = r, c

def inRange(x, y):
    return (0 <= x) and (x < n) and (0 <= y) and (y < n)

def isVisited(x, y):
    return visited[x][y]

def isSmaller(x, y, ref):
    return grid[x][y] < ref

def canGo(x, y, ref):
    return inRange(x, y) and not isVisited(x, y) and isSmaller(x, y, ref)



for _ in range(k): # k번 반복
    maxval = 0  
    visited = [[False for _ in range(n)] for _ in range(n)]

    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()

        for direction in directions:
            dx, dy = direction[0], direction[1]
            X, Y = x + dx, y + dy

            if canGo(X, Y, grid[r][c]):
                q.append((X, Y))
                visited[X][Y] = True

                if grid[X][Y] > maxval:
                    maxval = grid[X][Y]
                    sx, sy = X, Y

                elif grid[X][Y] == maxval:
                    if sx > X:
                        sx, sy = X, Y
                    
                    elif sx == X:
                        if sy > Y:
                            sx, sy = X, Y
    
    r, c = sx, sy

print(f'{sx+1} {sy+1}')