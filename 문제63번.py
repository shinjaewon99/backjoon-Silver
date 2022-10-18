# 두 리스트 합치기

from numpy import append


n = int(input())
a = list(map(int,input().split()))

m = int(input())
b = list(map(int,input().split()))

p1 = p2 = 0

arr = []

while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        arr.append(a[p1])
        p1+=1

    else:
        arr.append(b[p2])

        p2+=1

if p1 < n :
    arr = arr+a[p1:]

if p2< m:
    arr = arr+b[p2:]

for i in arr:
    print(i , end= ' ')