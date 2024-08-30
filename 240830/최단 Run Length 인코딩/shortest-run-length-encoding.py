import sys

def shiftOnce(x):
    x = list(x) # string은 값 변경이 불가능함, 리스트로 변경
    tmp = x[-1]

    for i in range(len(x)-1, 0, -1):
        x[i] = x[i-1] # shift 적용

    x[0] = tmp

    return ''.join(x) # list를 다시 string으로 변경

def runLengthEncoding(x): # 제일 중요한 부분
    result = ""
    i = 0 # 초기 인덱스

    while i < len(x): # 순회
        char = x[i] # 현재 기준 문자
        cnt = 1 # 카운트 1부터 시작

        while (i + 1 < len(x) and x[i+1] == char): # 다음 인덱스가 문자열 길이보다 작고, 다음 인덱스의 문자가 현재 기준 문자와 같을때까지 탐색
            cnt += 1
            i += 1
        
        result += char + str(cnt)
        i += 1 # 이렇게 하면 문자가 다른것부터 탐색 시작

    return len(result)

if __name__=="__main__":
    string = sys.stdin.readline().strip() # 문자열 입력받을땐 그냥 무조건 strip 사용하기

    if len(string) == 1: # 예외 처리
        print(2)

    else:
        min_length = []

        for _ in range(len(string)):
            string = shiftOnce(string)
            min_length.append(runLengthEncoding(string))
        
        print(min(min_length))