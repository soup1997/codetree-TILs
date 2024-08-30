import sys

def shiftOnce(x):
    tmp = x[-1]
    x = list(x) # string은 값 변경이 불가능함, 리스트로 변경
    
    for i in range(len(x)-1, 0, -1):
        x[i] = x[i-1] # shift 적용

    x[0] = tmp

    return ''.join(x) # list를 다시 string으로 변경

def runLengthEncoding(x):
    result = ""
    i = 0

    while i < len(x):
        char = x[i]
        cnt = 1

        while (i + 1 < len(x) and x[i+1] == char):
            cnt += 1
            i += 1
        
        result += char + str(cnt)
        i += 1

    return len(result)

if __name__=="__main__":
    string = sys.stdin.readline()

    if len(string) == 2:
        print(2)

    else:
        min_length = len(string)

        for _ in range(len(string)):
            string = shiftOnce(string)
            min_length = min(min_length, runLengthEncoding(string))
        
        print(min_length)