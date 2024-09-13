import sys

n = int(sys.stdin.readline())
m = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m.sort(key=lambda x: x[1])

cnt = 1
now = m[0][1]

for i in range(1, n): # 감탄스러운 코드다, i값을 전혀 건드릴 필요가 없다
    if now <= m[i][0]:
        cnt += 1
        now = m[i][1] # 조건 맞을때 만 기준 값을 바꾼다
    
print(cnt)