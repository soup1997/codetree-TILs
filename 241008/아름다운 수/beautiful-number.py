import sys

answer = 0
n = int(sys.stdin.readline())

def check(num_list):
    global answer

    flag = True
    for i in range(len(num_list)):
        standard = num_list[i]
        cnt = 0
        while(i < len(num_list) and standard == num_list[i]):
            cnt += 1
            i += 1
        
        if cnt != standard:
            flag = False

    if flag:
        answer += 1 
            

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