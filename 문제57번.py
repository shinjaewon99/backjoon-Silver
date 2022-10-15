# 뒤집은 소수 , 그 소수가 약수인지 판별


def reverse(i):
    res = 0
    while i >0:
        t = i % 10
        res = res * 10 + t
        i = i// 10
    
    return res

def isPrime(i):
    if i == 1 :
        return False
    for j in range(2, i // 2+1):
        if i % j == 0:
            return False
        
    else:
        return True



n = int(input())
arr = list(map(int,input().split()))




for i in arr:
    tmp =reverse(i)

    if isPrime(tmp):
        print(tmp , end=' ')





