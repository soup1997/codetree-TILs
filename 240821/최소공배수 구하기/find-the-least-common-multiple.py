n, m = map(int, input().split())

for i in range(2, m+1):
    if (n % i == 0) and (m % i == 0):
        maximum = i

a = n / maximum
b = m / maximum
c = maximum

res = int(a*b*c)
print(res)