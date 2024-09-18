import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

maximum = -1000 # 제한 조건에서 가장 작은 원소의 값
total = 0

for i in range(len(sequence)):
    total += sequence[i]
    maximum = max(maximum, total)

    if total < 0:
        total = 0

print(maximum)