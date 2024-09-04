import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
vertices = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
visited = [[False for _ in range(n)] for _ in range(n)]
directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [0, 0]]
q = deque()
cnt = 0

def inRange(x, y):
    return (0 <= x) and (x < n) and (0 <= y) and (y < n)

def isVisited(x, y):
    return visited[x][y]

def isZero(x, y):
    return grid[x][y] == 0

def canGo(x, y):
    return inRange(x, y) and not isVisited(x, y) and isZero(x, y)

def bfs(start_x, start_y):
    global cnt, directions, q

    q.append((start_x, start_y))

    while q:
        x, y = q.popleft()

        for direction in directions:
            dx, dy = direction[0], direction[1]
            X, Y = x + dx, y + dy

            if canGo(X, Y):
                visited[X][Y] = True
                cnt += 1
                q.append((X, Y))


if __name__=="__main__":
    for vertex in vertices:
        x, y = (vertex[0] - 1) , (vertex[1] - 1)
        bfs(x, y)
    
    print(cnt)