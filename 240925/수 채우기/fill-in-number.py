import sys

MAX_NUM = 50000

# 변수 선언 및 입력:
n = int(sys.stdin.readline())
ans = MAX_NUM

# 사용할 5원 동전의 수를 전부 가정해보며
# 그 중 가장 좋은 선택을 합니다.
for i in range(MAX_NUM + 1):
    remainder = n - 5 * i
    if remainder >= 0 and remainder % 2 == 0:
        ans = min(ans, i + (remainder // 2))

# 만약 그러한 동전을 만드는 것이 불가능하다면
# -1을 넣어줍니다.
if ans == MAX_NUM:
    ans = -1

print(ans)