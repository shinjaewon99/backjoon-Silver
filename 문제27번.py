# 1980번

n = int(input())
m = int(input())

num = list(map(int,input().split()))
num.sort()

cnt = 0

i,j = 0,n-1

while i < j:
    if num[i] + num[j] ==m:
        cnt +=1
        i +=1
        j -=1

    elif num[i] + num[j] <m:
        i +=1

    else :
        j -=1

print(cnt)