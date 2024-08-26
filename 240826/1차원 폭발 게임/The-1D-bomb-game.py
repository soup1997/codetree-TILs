import sys

# input
n, m = map(int, sys.stdin.readline().split())
vec = [int(sys.stdin.readline()) for _ in range(n)]


cnt = 1

for i in range(n-1):
    if vec[i] == vec[i+1]:
        cnt += 1

        if cnt >= m:
            cnt = 1
            j = i+1

            while (j < n) and (vec[i] == vec[j]): # find until same element appears
                j += 1

            vec[i:j] = [0 for _ in range(j-i)] # explosion

            for k in range(n-2):
                if vec[k] != 0:
                    vec[k+1] = vec[k]
                    vec[k] = 0

    else:
        cnt = 1

if m == 1:
    print(0)

else:
    print(len(vec) - vec.count(0))
    for i in vec:
        if i != 0:
            print(i)