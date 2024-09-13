import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
cost = 0

while len(arr) >= 2:
    first_idx = arr.index(min(arr))
    first_min = arr.pop(first_idx)

    second_idx = arr.index(min(arr))
    second_min = arr.pop(second_idx)

    res = first_min + second_min
    cost += (res)
    arr.append(res)

print(cost)