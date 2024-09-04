import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
q = deque()

def inRange(x, y):
    return (0 <= x) and (x < n) and (0 <= y) and (y < m)

def isVisit(x, y):
    return visited[x][y]

def isSnake(x, y):
    return grid[x][y] == 0

def canGo(x, y):
    return inRange(x, y) and not isVisit(x, y) and not isSnake(x, y)

def bfs():
    q.append((0, 0)) # root를 queue에 push
    visited[0][0] = True # root를 방문 처리하고 시작

    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우 인접 4방향

    while q: # queue가 빌때까지 계속해서 탐색
        x, y = q.popleft() # 현재 기준 위치

        for direction in directions: # 현재 기준위치 인접 4방향 탐색
            dx, dy = direction[0], direction[1]
            X, Y = x + dx, y + dy

            if canGo(X, Y): # 그리드 안에 존재하고, 방문하지 않았고, 뱀이 없다면
                visited[X][Y] = True # 방문 처리
                q.append((X, Y)) # queue에 push

if __name__=='__main__':
    bfs()
    print(1) if visited[-1][-1] else print(0)