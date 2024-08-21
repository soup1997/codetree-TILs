Y, M, D = map(int, input().split())

def check(Y):
    if Y % 4 == 0:
        if Y % 100 == 0:
            
            if Y % 400 == 0:
                return True
            
            else:
                return False
        
        else:
            return True
    
    else:
        return False
    
res = check(Y)

if res and M == 2 and D == 28:
    print(-1)

else:
    if M in [3, 4, 5]:
        print("Spring")

    elif M in [6, 7, 8]:
        print("Summer")

    elif M in [9, 10, 11]:
        print("Fall")

    elif M in [12, 1, 2]:
        print("Winter")