import sys

# input
n, m = map(int, sys.stdin.readline().split())
vec = [int(sys.stdin.readline()) for _ in range(n)]

n, m = 5 ,2
vec = [1, 2, 2, 1, 1]


cnt = 1

for i in range(n-1):
    if vec[i] == vec[i+1]:
        cnt += 1
        if cnt >= m:
            vec[i:i+cnt] = [0 for _ in range(cnt)] # explosion
            for j in range(i+cnt-1): # shift
                if vec[j] != 0:
                    vec[j+1] = vec[j]
                    vec[j] = 0
            
            cnt = 1 # count initialization

    else:
        cnt = 1

if m == 1:
    print(0)

else:
    print(len(vec) - vec.count(0))
    for i in vec:
        if i != 0:
            print(i)