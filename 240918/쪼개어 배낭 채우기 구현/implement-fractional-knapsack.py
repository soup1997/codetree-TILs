import sys

n, m = map(int, sys.stdin.readline().split()) # m 이 가방의 무게
jewels = []

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    ratio = round(v / w, 3) # 무게 대비 가치가 높은 보석이 최우선 순위
    jewels.append([w, v, ratio]) # 무게, 가치, 비율

jewels.sort(key=lambda x: x[2], reverse=True) # 내림차순 정렬

total = 0 # 훔치려는 보석들의 총 가치
for jewel in jewels:
    w, v = jewel[0], jewel[1]
    
    if m == 0:
        break

    else:
        if m >= w:
            m -= w
            total += v
        
        else:
            total += v * (m / w)
            m = 0 # 현재 보석을 쪼개서 가방을 다 채워야 함

print(f'{total:.3f}')