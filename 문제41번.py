# 1417번

n = int(input())
d = int(input())
arr = []
cnt = 0


for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

if n == 1:
    print(0)

else :

    while arr[0] >= d:
        d +=1
        arr[0] -=1
        cnt +=1
        arr.sort(reverse=True)

    print(cnt)