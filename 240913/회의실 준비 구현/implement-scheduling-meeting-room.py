import sys

n = int(sys.stdin.readline())
m = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m.sort(key=lambda x: x[1])

idx = 0
cnt = 0
while idx < len(m)-1:
    if m[idx][1] <= m[idx+1][0]:
        cnt += 1
        idx += 1

    else:
        before_end = m[idx][1]

        while idx < len(m)-1 and before_end > m[idx+1][0]:
            idx += 1
        
        cnt += 1

print(cnt)