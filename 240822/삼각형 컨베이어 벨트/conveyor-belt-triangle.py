import sys
n, t = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

# convert into 1D vector
vec = [j for i in arr for j in i]

for _ in range(t):
    tmp = vec[-1]
    for i in range(len(vec)-1, 0, -1):
        vec[i] = vec[i-1]
    
    vec[0] = tmp

print(*vec[:n])
print(*vec[n:2*n])
print(*vec[2*n:3*n])