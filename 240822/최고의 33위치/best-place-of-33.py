N = int(input())

arr = []
for i in range(N):
    vec = list(map(int, input().split()))
    arr.append(vec)

def search(x, y, dx, dy):
    num = 0

    for i in range(x, dx+1):
        for j in range(y, dy+1):
            if arr[i][j] == 1:
                num += 1


max_gold = 0

for i in range(N):
    for j in range(N):
        if i + 2 >= N or j + 2 >= N:
            continue

        num_of_gold = serach(i, j, i+2, j+2)

        max_gold = max(max_gold, num_of_gold)

print(max_gold)