n, m, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
k -= 1

# 해당 row에 [col_s, col_e] 열에
# 전부 블럭이 없는지를 확인합니다.
def all_blank(row, col_s, col_e):
    return all([not grid[row][col_s: col_e+1]])


# 최종적으로 도달하게 될 위치는
# 그 다음 위치에 최초로 블럭이 존재하는 순간임을 이용합니다.
def get_target_row():
    for row in range(n - 1):
        if not all_blank(row + 1, k, k + m - 1):
            return row

    return n - 1

target_row = get_target_row()
grid[target_row][k, k + m] = [1] * m

for i in range(n):
    print(* grid[i], end=" ")