import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
r, c = map(int, sys.stdin.readline().split())

r, c = r-1, c-1
size = (arr[r][c]) - 1


# explosion
for i in range(max(0, r-size), min(n, r+1+size)):
    for j in range(max(0, c-size), min(n, c+1+size)):       
        if j > n-1:
            break

        if j == c or i == r:
            arr[i][j] = 0 # 폭발

# arrangement
for col in range(n):
    for row in range(n-1, 0, -1):
        if arr[row][col] == 0:
            start = row # 가장 마지막 행 부터 검사

            while start != -1:
                if arr[start][col]: # 값이 0이 아니라면
                    arr[row][col] = arr[start][col] # shift
                    arr[start][col] = 0 # shift 되었으므로 0으로 대체
                    break
                
                else:
                    start -=1


for vec in arr:
    print(*vec)