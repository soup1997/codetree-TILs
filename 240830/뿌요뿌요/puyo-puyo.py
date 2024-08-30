import sys
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range (n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def inRange(x, y):
    return (0 <= x) and (x < n) and (0 <= y) and (y < n)

def notVisited(x, y):
    return not visited[x][y]

def isSame(x, y, val):
    return grid[x][y] == val

def canGo(x, y, val):
    return inRange(x, y) and notVisited(x, y) and isSame(x, y, val)

def DFS(x, y, val):
    global dfs_cnt

    dfs_cnt += 1 # DFS 호출될때마다 카운트 +1
    visited[x][y] = True

    for direction in directions:
        dx, dy = direction[0], direction[1]
        X, Y = x + dx, y + dy

        if canGo(X, Y, val):
            DFS(X, Y, val)
    
    if dfs_cnt >= 4: # DFS가 4번이상 실행되면 블록 1개 존재
        return 1
    
    else: # 블록 없음
        return 0


if __name__=="__main__":
    block_cnt = 0 # 블록 카운트 변수
    dfs_cnt = 0 # DFS 가 몇번 실행되는지 카운트하는 변수
    max_block = 0

    for i in range(n):
        for j in range(n):
            block_cnt += DFS(i, j, grid[i][j])
            max_blobk = max(dfs_cnt, max_block)
            dfs_cnt = 0

    print(block_cnt, max_blobk)