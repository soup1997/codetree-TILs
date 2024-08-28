import sys

'''
O-------> Y
|
|
|
v
X
'''

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 그리드 생성
visited = [[False for _ in range(m)] for _ in range(n)] # grid의 (행, 열)마다 visited 표시를 위한 2차원 배열
visited[0][0] = True # 시작점이므로 방문 표시

def inRange(newX, newY): # grid 범위 내 인지 검사
    return (0 <= newX) and (newX < n) and (0 <= newY) and (newY < m)

def snake(newX, newY): # 해당 grid에 뱀이 있는지 검사
    answer = True if grid[newX][newY] == 1 else False
    return answer

def visitCheck(newX, newY): # 방문하지 않은 grid인지 검사
    answer = True if visited[newX][newY] == False else False
    return answer

def can_go(newX, newY): # 이동 여부 체크
    return (inRange(newX, newY)) and (snake(newX, newY)) and (not visitCheck(newX, newY))

def DFS(x, y):
    dxs, dys = [1, 0], [0, 1] # 아래, 우측으로만 이동

    for dx, dy in zip(dxs, dys): # 현재 grid 기준으로 아래, 우측 인접한 grid 하나씩 확인
        newX, newY = x + dx, y + dy

        if can_go(newX, newY):
            visited[newX][newY] = True

            if visited[-1][-1]: # 탐색 종료
                break       

            else: # 탐색 계속
                DFS(newX, newY)

if __name__=="__main__":
    startX, startY = 0, 0 # 초기 시작 위치
    DFS(startX, startY)
    print(1) if visited[-1][-1] else print(0)