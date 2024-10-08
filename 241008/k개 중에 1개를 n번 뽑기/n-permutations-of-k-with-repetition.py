import sys

def choose():
    global answer
    
    # 종료 조건
    if len(answer) == n: 
        print(*answer)
        return
    
    # 재귀 조건
    for i in range(1, k + 1):
        answer.append(i)
        choose()  # Recursive call with next number
        answer.pop()  # Backtrack to try other numbers

k, n = map(int, sys.stdin.readline().split())
answer = []
choose()