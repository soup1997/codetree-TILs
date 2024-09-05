import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
q = deque([i for i in range(1, N+1)])

while q:
    for _ in range(K-1):
        q.append(q.popleft())
    print(q.popleft(), end=' ')