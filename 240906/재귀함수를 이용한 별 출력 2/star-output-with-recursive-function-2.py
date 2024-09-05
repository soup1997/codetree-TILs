import sys

n = int(sys.stdin.readline())

def printStar(n):
    if n == 0:
        return 
    
    else:
        print('* ' * n)
        printStar(n-1)
        print("* " * n)

printStar(n)