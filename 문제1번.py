# 1010번

t = int(input())

def factorial(x):
    cnt = 1

    for i in range(2, x+1):
        cnt *= i 

    
    return cnt

for j in range(t):

    a,b = map(int,input().split())
    res = factorial(b) // (factorial(a) * factorial(b-a))
    print(res)