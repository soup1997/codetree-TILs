import sys

answer = 0
n = int(sys.stdin.readline())

# 아름다운 수 인지 확인하는 함수
def check(num_list):
    global answer
    flag = True
    i = 0
    
    while i < len(num_list):
        standard = num_list[i]
        cnt = 0
        while i < len(num_list) and standard == num_list[i]:
            cnt += 1
            i += 1        
        if (cnt != standard) and (cnt % standard != 0): # 반례 추가, 111인경우 1이 1번 나온것이 3번반복되었으므로 아름다운 수
            flag = False
    if flag:
        answer += 1
            

# back tracking
def makeBeautifulNum():
    global num

    if len(num) == n:
        check(num)
        return

    else:
        for i in range(1, 5):
            num.append(i)
            makeBeautifulNum()
            num.pop()

num = []
makeBeautifulNum()
print(answer)