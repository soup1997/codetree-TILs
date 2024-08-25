import sys

n, m = map(int, sys.stdin.readline().split())

bombs = [int(sys.stdin.readline()) for _ in range(n)]

def explosion(bombs, m):
    if m == 1:
        return []
    
    else:
        cnt = 1

        for i in range(len(bombs)-1):
            try:
                if bombs[i] == bombs[i+1]:
                    cnt += 1

                    if cnt >= m:
                        del bombs[i:i+cnt]
                        
                
                else:
                    cnt = 1

            except IndexError:
                explosion(bombs, m)


        return bombs


res = explosion(bombs, m)

print(len(res))

if len(res):
    for i in range(len(res)):
        print(res[i])