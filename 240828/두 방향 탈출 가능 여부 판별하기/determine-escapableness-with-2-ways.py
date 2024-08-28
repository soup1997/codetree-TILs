import sys

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 그리드 생성
visited = [[False for _ in range(m)] for _ in range(n)] # grid의 (행, 열)마다 visited 표시를 위한 2차원 배열
visited[0][0] = True # 시작점이므로 방문 표시
dxs, dys = [1, 0], [0, 1] # 아래, 우측으로만 이동

def inRange(newX, newY): # grid 범위 내 인지 검사
    return (0 <= newX) and (newX <= n) and (0 <= newY) and (newY <= m)

def snake(newX, newY): # 해당 grid에 뱀이 있는지 검사
    answer = True if grid[newX][newY] else False
    return answer

def visitCheck(newX, newY): # 방문한 grid인지 검사
    answer = True if visited[newX][newY] else False
    return answer

def can_go(newX, newY): # 이동 여부 체크
    return inRange(newX, newY) and snake(newX, newY) and visitCheck(newX, newY)

def DFS(currX, currY):
    for dx, dy in zip(dxs, dys): # 현재 grid에서 아래, 우측인접한 grid 확인
        newX, newY = currX + dx, currY + dy

        if can_go(newX, newY):
            visited[newX][newY] = True
            DFS(newX, newY)


if __name__=="__main__":
    x, y = 0, 0 # 초기 시작 위치
    DFS(x, y)
    print(1) if visited[-1][-1] else print(0)