# 8974번

n , m = map(int,input().split())

arr = []

for i  in range(1, m+1):
    if len(arr) < m :
        for j in range(i):
            arr.append(i)


print(sum(arr[n-1:m]))