import sys
sys.setrecursionlimit(10000) # 재귀 리미트는 디폴트가 1000임, 재귀 이용해서 문제를 풀 경우 limit 범위 늘릴 것

n, m = map(int, sys.stdin.readline().split())
grid = []

maximum = 1
minimum = 1

for _ in range(n): # grid 만들기
    vec = list(map(int, sys.stdin.readline().split()))
    grid.append(vec)
    maximum = max(max(vec), maximum)
    minimum = min(min(vec), minimum)

directions = [[-1, 0], # 상
              [1, 0], # 하
              [0, -1], # 좌
              [0, 1]] # 우


def inRange(x, y):
    return (0 <= x) and (x < n) and (0 <= y) and (y < m)

def isSinking(x, y, k):
    return grid[x][y] <= k

def checkVisited(x, y):
    return not visited[x][y]

def canGo(x, y, k):
    return inRange(x, y) and (not isSinking(x, y, k)) and (checkVisited(x, y))

def DFS(x, y, k):
    visited[x][y] = True

    # x, y 기준 인접 4개의 방향에 대한 그리드 탐색
    for direction in directions:
        dx, dy = direction[0], direction[1]
        X, Y = x + dx, y + dy

        if canGo(X, Y, k):
            visited[X][Y] = True
            DFS(X, Y, k)
    
    return 1


if __name__=='__main__':
    if maximum == 1:
        print(1, 0)

    else:
        data = {}
        for k in range(minimum, maximum):
            cnt = 0
            visited = [[False for _ in range(m)] for _ in range(n)]

            for i in range(n):
                for j in range(m):
                    if canGo(i, j, k):
                        cnt += DFS(i, j, k)
                        
            data[k] = cnt
        
        max_value = max(data.values()) # dictionary에서 value 기준으로 minimum값을 찾기
        for key, value in data.items(): # 순회하면서 minimum value인 key를 찾기
            if value == max_value: # 가장 작은 k값을 출력해야하므로 찾으면 탐색 중지 
                print(key, value)
                break