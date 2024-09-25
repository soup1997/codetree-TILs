import sys
n = int(sys.stdin.readline())
price = list(map(int, sys.stdin.readline().split()))

profit = 0

# 가장 쌀 때 사서 가장 비싸게 파는 것이 목적
# 단, 년도는 역행이 불가능함

for i in range(len(price)-1):
    for j in range(i+1, len(price)):
        if price[j] - price[i] > 0:
            profit = max(profit, price[j] - price[i])

print(profit)