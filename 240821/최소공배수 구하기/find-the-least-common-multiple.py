n, m = map(int, input().split())

for i in range(2, m+1):
    if (n % i == 0) and (m % i == 0):
        maximum = i

print(int(n/maximum * m/maximum * maximum))