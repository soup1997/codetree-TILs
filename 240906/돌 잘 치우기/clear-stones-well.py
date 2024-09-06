import sys
import copy
from collections import deque

n, k, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def inRange(x, y):
    return (0 <= x) and (x < n) and (0 <= y) and (y < n)

def canVisit(x, y):
    return not visited[x][y]

def isZero(x, y):
    global delete_cnt, m

    if delete_cnt < m and grid_copy[x][y] == 1:
        grid_copy[x][y] = 0
        delete_cnt += 1

    return grid_copy[x][y] == 0

def canGo(x, y):
    return inRange(x, y) and canVisit(x, y) and isZero(x, y)

def bfs(sx, sy):
    cnt = 1
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

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

if __name__=='__main__':
    cnt_list = []
    delete_cnt = 0

    for _ in range(k):
        grid_copy = copy.deepcopy(grid) # deep copy
        sx, sy = map(int, sys.stdin.readline().split())
        visited = [[False] * n for _ in range(n)]
        cnt_list.append(bfs(sx-1, sy-1))
        delete_cnt = 0

    print(max(cnt_list))