import sys
from functools import cmp_to_key

def compare(x, y):
    s1 = x + y
    s2 = y + x

    if int(s1) > int(s2): # x가 먼저 오게 정렬
        return -1
    
    elif int(s1) < int(s2): # y가 먼저 오게 정렬
        return 1
    
    else: # x, y 순서 그대로 유지
        return 0

n = int(sys.stdin.readline())
arr = [sys.stdin.readline().strip() for _ in range(n)]
arr.sort(key=cmp_to_key(compare))

print(*arr, sep="")