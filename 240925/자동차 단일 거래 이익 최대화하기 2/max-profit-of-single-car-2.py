import sys
n = int(sys.stdin.readline())
price = list(map(int, sys.stdin.readline().split()))

profit = 0
min_price = float('inf')

for p in price:
    min_price = min(min_price, p)
    profit = max(profit, p - min_price)

print(profit)