import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
candidate = []

total = 0
for i in range(len(sequence)):
    total += sequence[i]

    if i == len(sequence) - 1:
        candidate.append(total)

    elif total < 0:
        candidate.append(total - sequence[i])
        total = 0

print(max(candidate))