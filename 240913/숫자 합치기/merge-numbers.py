import sys
import heapq # 힙을 이용해서 빠르게 최소값을 찾아내자!

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
heapq.heapify(arr)
cost = 0

while len(arr) >= 2:
    first_min = heapq.heappop(arr)
    second_min = heapq.heappop(arr)
    res = first_min + second_min
    heapq.heappush(arr, res)
    cost += (res)

print(cost)