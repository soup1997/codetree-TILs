def row_search(row):
    check = 0
    for j in range(n):
        if arr[row][:].count(arr[row][j]) >= m:
            check += 1
    
    return check

def col_search(col):
    check = 0
    for i in range(n):
        if arr[:][col].count(arr[i][col]) >= m:
            check += 1
    
    return check

# make grid
n, m = map(int, input().split())
arr = []
for i in range(n):
    vec = list(map(int, input().split()))
    arr.append(vec)

# find happy sequence
row_check = 0
col_check = 0

for i in range(n):
    row_check += row_search(row=i)
    col_check += col_search(col=i)

print(row_check + col_check)