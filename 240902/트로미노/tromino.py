import sys

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 가능한 블록의 경우의 수 (가운데 위치한 블록을 기준으로)

up = [-1, 0]
down = [1, 0]
left = [0, -1]
right = [0, 1]

blocks = [[up, right],
          [up, left],
          [down, left],
          [down, right],
          [left, right],
          [up, down]]

def inRange(x, y):
    return (0 <= x) and (x < n) and (0 <= y) and (y < m)

def calcSum(x, y):
    totalList = []

    for block in blocks:
        cnt = 0
        for direction in block:
            dx, dy = direction[0], direction[1]
            X, Y = x + dx, y + dy

            if inRange(X, Y):
                cnt += 1
            
            if cnt == 2:
                total = grid[x][y]
                for direction in block:
                    dx, dy = direction[0], direction[1]
                    X, Y = x + dx, y + dy
                    total += grid[X][Y]

                totalList.append(total)
                cnt = 0

    return max(totalList)

if __name__=='__main__':
    total_list = []
    for i in range(n):
        for j in range(m):
            total_list.append(calcSum(i, j))
    
    print(max(total_list))