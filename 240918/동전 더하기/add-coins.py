import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
idx, cnt = len(coins)-1, 0

while k != 0:
    cnt += k // coins[idx]
    k %= coins[idx]
    idx -= 1

print(cnt)