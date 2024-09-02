import sys

n, r, c = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 우선 순위(상하좌우)

r, c = r-1, c-1
row, column = r, c

def inRange(x, y):
    return (0 <= x) and (x < n) and (0 <= y) and (y < n)

def search(r, c):
    global row, column

    for direction in directions:
        dx, dy = direction[0], direction[1]
        x, y  = r + dx, c + dy

        if inRange(x, y):
            if grid[x][y] > grid[r][c]: # 인접한 4칸중에 기준 칸보다 값이 크다면
                print(grid[x][y], end=" ") # 인접한 칸 출력
                search(x, y) # 재귀 돌리기
                break # 재귀 끝나면 다음 direction을 볼 필요가 없음
            

print(grid[r][c], end=" ") # 첫 방문 지점 출력
search(r, c)