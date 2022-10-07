# 17219번

n , m = map(int,input().split())

arr = {}

for i in range(n):
    a ,b = input().split()

    arr[a] = b

for j in range(m):
    print(arr[input().rstrip()])