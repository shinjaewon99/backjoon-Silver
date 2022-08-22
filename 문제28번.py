# 2847번

n = int(input())

arr =[]

total = 0

for i in range(n):
    arr.append(int(input()))


for j in range(n-1 , 0 , -1):


    if arr[j] <= arr[j-1]:
        total += (arr[j-1] - arr[j]+1)
        arr[j-1] = arr[j] -1

print(total)