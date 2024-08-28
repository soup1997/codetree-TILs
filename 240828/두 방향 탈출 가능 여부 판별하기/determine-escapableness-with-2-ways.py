import sys

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
visited[0][0] = True

x, y = 0, 0
dxs, dys = [1, 0], [0, 1]

def inRange(newX, newY):
    return (0 <= newX) and (newX <= n) and (0 <= newY) and (newY <= m)

def snake(newX, newY):
    answer = True if grid[newX][newY] else False
    return answer

def visitCheck(newX, newY):
    answer = True if visited[newX][newY] else False
    return answer

def can_go(newX, newY):
    return inRange(newX, newY) and snake(newX, newY) and visitCheck(newX, newY)

def DFS(cx, cy):
    for dx, dy in zip(dxs, dys):
        newX, newY = cx + dx, cy + dy

        if can_go(newX, newY):
            visited[newX][newY] = 1
            DFS(newX, newY)

print(1) if visited[-1][-1] else print(0)