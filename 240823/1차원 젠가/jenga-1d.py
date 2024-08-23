import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

for _ in range(2):
    start, end = map(int, sys.stdin.readline().split())
    tmp = []

    for i in range(len(arr)):
        if (i < start-1) or (i > end-1):
            tmp.append(arr[i])
    
    arr = tmp

print(len(arr))
for i in arr:
    print(i)