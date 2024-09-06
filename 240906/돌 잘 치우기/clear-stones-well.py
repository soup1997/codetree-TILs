import sys
import copy
from collections import deque
from itertools import combinations

# 입력 받기
n, k, m = map(int, sys.stdin.readline().split())
grid, rockList = [], []
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 그리드와 돌의 위치 입력 받기
for i in range(n):
    vec = list(map(int, sys.stdin.readline().split()))
    grid.append(vec)
    for j in range(len(vec)):
        if vec[j] == 1:
            rockList.append((i, j))  # 돌의 위치 저장

start_points = []
for _ in range(k):
    sx, sy = map(int, sys.stdin.readline().split())
    start_points.append((sx - 1, sy - 1))  # 시작점 저장, 인덱스를 0부터 사용하기 위해 -1

# 범위 확인 함수
def inRange(x, y):
    return (0 <= x) and (x < n) and (0 <= y) and (y < n)

# 방문 여부 및 도달 가능 여부 확인 함수
def canVisit(x, y):
    return not visited[x][y]

def isZero(x, y):
    return grid_copy[x][y] == 0

def canGo(x, y):
    return inRange(x, y) and canVisit(x, y) and isZero(x, y)

# BFS 탐색
def bfs():
    cnt = 0
    q = deque()

    # 모든 시작점에서 BFS 시작
    for sx, sy in start_points:
        q.append((sx, sy))
        visited[sx][sy] = True
        cnt += 1

    # BFS 탐색
    while q:
        x, y = q.popleft()

        for direction in directions:
            dx, dy = direction[0], direction[1]
            nx, ny = x + dx, y + dy

            if canGo(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    
    return cnt

# 백트래킹을 통해 돌을 제거하는 경우의 수를 모두 시도
def solve():
    max_cnt = 0
    
    # 돌 리스트에서 m개의 돌을 제거하는 모든 조합을 확인
    for remove_rocks in combinations(rockList, m):
        # 그리드를 복사해서 사용할 deep copy
        global grid_copy, visited
        grid_copy = copy.deepcopy(grid)
        
        # 선택된 m개의 돌을 제거
        for x, y in remove_rocks:
            grid_copy[x][y] = 0  # 돌 제거
        
        # BFS로 도달 가능한 영역 계산
        visited = [[False] * n for _ in range(n)]
        max_cnt = max(max_cnt, bfs())  # 최대값 업데이트
    
    return max_cnt

# 결과 출력
print(solve())