import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))
total = 0

for i in nums:
    total += i

    if total < 0:
        total = i

print(total)