import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
cost = 0

while len(arr) >= 2:
    arr.sort() # 정렬 먼저 시작

    res = arr[0] + arr[1]
    cost += (res)

    arr.pop(0)
    arr.pop(0)
    arr.append(res)

print(cost)