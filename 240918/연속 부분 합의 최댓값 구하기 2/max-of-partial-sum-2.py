import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
candidate = []

total = 0
for i in range(len(sequence)):
    total += sequence[i]

    if total < 0:
        candidate.append(total - sequence[i])
        total = 0

    if i == len(sequence) - 1:
        candidate.append(total)

print(max(candidate))