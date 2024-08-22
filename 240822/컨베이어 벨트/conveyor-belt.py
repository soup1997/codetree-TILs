import sys

n, t = map(int, sys.stdin.readline().split())

arr = []
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# convert into 1D vector
arr = [j for i in nums for j in i]

# shift
for _ in range(t):
    tmp = arr[-1]

    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i - 1]
    
    arr[0] = tmp

print(*arr[:n])
print(*arr[n:])