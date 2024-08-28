import sys

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

directions = [[-1, 0], # up
              [1, 0], # down
              [0, -1], # left
              [0, 1]] # right

def inRange(x, y): # grid 내부 인지 확인
    return  (0 <= x) and (x < n) and (0 <= y) and (y < n)

def isPerson(x, y): # 사람인지 확인
    return grid[x][y] == 1

def checkVisited(x, y): # 방문한 곳인지 확인
    return visited[x][y] == False

def can_go(x, y): # 탐색할 수 있는 지점인지 확인
    return (inRange(x, y)) and (isPerson(x, y)) and (checkVisited(x, y))

def DFS(x, y):
    global numPerson

    for direction in directions:
        dx, dy = direction[0], direction[1]
        X, Y = x + dx, y + dy

        if can_go(X, Y):
            numPerson += 1
            visited[X][Y] = True
            DFS(X, Y)
    
    return 1 # 재귀 탐색 끝나면 마을 1개 카운트 완료

if __name__=="__main__":
    numTown = 0
    numPerson = 1
    people = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j] == 1:
                startX, startY = i, j
                numTown += DFS(startX, startY)
                people.append(numPerson)
                numPerson = 1
    people.sort()

    print(numTown)
    for i in people:
        print(i)