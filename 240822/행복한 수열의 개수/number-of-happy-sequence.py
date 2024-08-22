def row_search(row):
    cnt = 1
    for j in range(1, n):
        if arr[row][j-1] == arr[row][j]:
            cnt += 1
    
            if cnt >= m:
                return 1
    
    return 0

def col_search(col):
    cnt = 1
    for i in range(1, n):
        if arr[i-1][col] == arr[i][col]:
            cnt += 1

            if cnt >= m:
                return 1
    return 0

# make grid
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

if m == 1:
    print(2*n)

else:
    # find happy sequence
    row_check = 0
    col_check = 0

    for i in range(n):
        row_check += row_search(row=i)
        col_check += col_search(col=i)

    print(row_check + col_check)