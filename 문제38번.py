# 14659번

n = int(input())

arr= list(map(int,input().split()))

max = 0

for i in range(n):
    cnt = 0

    for j in range(1,n-i):
        if arr[i] >= arr[i+j]:
            cnt +=1

        else:
            break

    if max < cnt:
        max = cnt

print(max)
