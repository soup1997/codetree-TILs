import sys

n = int(sys.stdin.readline())
coins = 0

if (n % 5) % 2 != 0:
    print(-1)

else:
    coins += n // 5
    coins += (n % 5) // 2
    print(coins)