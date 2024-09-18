import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
candidate = []
total = 0

for i in range(len(sequence)):
    total += sequence[i]

    if total < 0:
        total -= sequence[i]
        candidate.append(total)
        total = 0
candidate.append(total)
print(max(candidate))