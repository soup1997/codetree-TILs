import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력
n = int(input())
arr = [0] + list(map(int, input().split()))

# 최댓값을 구해야 하는 문제이므로
# 초기값을 INT_MIN으로 설정합니다.
ans = INT_MIN

# 현재 연속 부분 수열 내 원소의 합을
# 저장합니다.
sum_of_nums = 0;

for i in range(1, n + 1):
    # 만약 현재 연속 부분 수열 내 원소의 합이
    # 0보다 작아진다면, 지금부터 새로운
    # 연속 부분 수열을 만드는 것이 더 유리합니다.
    if sum_of_nums < 0:
        sum_of_nums = arr[i]
    
    # 그렇지 않다면 기존 연속 부분 수열에 
    # 현재 원소를 추가하는 것이 더 좋습니다.
    else:
        sum_of_nums += arr[i]
    
    ans = max(ans, sum_of_nums)

print(ans)