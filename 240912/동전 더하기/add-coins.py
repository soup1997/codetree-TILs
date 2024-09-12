import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline().strip()) for _ in range(n)]

cnt = 0
idx = len(coins)-1

while k != 0 and idx >= 0:
    cnt += k // coins[idx]
    k %= coins[idx]
    idx -=1

print(cnt)