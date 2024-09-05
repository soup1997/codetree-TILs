# 조건 1: k번 만큼 반복하며 bfs를 수행해야 함
# 조건 2: 기록해 둔 시작 위치의 값보다 작은 값 중에 제일 큰 값과 그 좌표를 갱신해야함
# 조건 3: 제일 큰 값을 가진 좌표가 여러개일 경우 먼저 행이 작은 순서대로 고려하고 그 다음 열이 작은 순서대로 고려해서 시작점을 갱신해야함

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
grid = [(list(map(int, sys.stdin.readline().split()))) for _ in range(n)]
r, c = map(int, sys.stdin.readline().split())
r, c = r-1, c-1 # 1씩 빼서 받기
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 인접 4방향

sx, sy = r, c # 시작 기준 좌표

def inRange(x, y): # grid 바깥을 넘어가지 않는지 검사
    return (0 <= x) and (x < n) and (0 <= y) and (y < n)

def isVisited(x, y): # 방문한 좌표인지 검사
    return visited[x][y]

def isSmaller(x, y, ref): # 기준 좌표보다 작은 값을 가지고 있는지 검사
    return grid[x][y] < ref

def canGo(x, y, ref): # 3가지 조건을 모두 충족해야 함
    return inRange(x, y) and not isVisited(x, y) and isSmaller(x, y, ref)

for _ in range(k):
    maxval = 0 # grid 내에 1이상 100이하의 숫자만 존재하므로 0으로 초기화
    visited = [[False for _ in range(n)] for _ in range(n)] # visited 초기화

    # bfs 시작
    q = deque()
    q.append((sx, sy)) # 기준 좌표 넣고 시작
    visited[sx][sy] = True # 기준 좌표 방문 처리

    while q: # queue가 빌때까지 계속 반복
        x, y = q.popleft()

        for direction in directions: # 인접 4방향 검사
            dx, dy = direction[0], direction[1]
            X, Y = x + dx, y + dy

            if canGo(X, Y, grid[r][c]):
                q.append((X, Y))
                visited[X][Y] = True

                # maxval 값이 하나라면 
                if grid[X][Y] > maxval: # 현재 탐색하고 있는 좌표값이 maxval보다 크다면
                    maxval = grid[X][Y] # maxval 업데이트, 애초에 canGo에서 기준좌표 값 보다 작은 값만 움직이게 했으므로 기준 좌표 값보다 무조건 작은 값임
                    sx, sy = X, Y # 해당 최댓값을 다음 for문 시작 좌표로 설정

                # maxval 값이 두개 이상이라면
                elif grid[X][Y] == maxval:
                    if sx > X: # 현재 탐색 x좌표가 시작 x좌표보다는 무조건 작아야 함 (우선순위 1)
                        sx, sy = X, Y
                    
                    else: # 현재 탐색 x좌표와 시작 x좌표값과 같다면 (우선순위 2)
                        if sy > Y: # 현재 탐색 
                            sx, sy = X, Y
    
    r, c = sx, sy

print(f'{sx+1} {sy+1}')