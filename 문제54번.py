# k번째 큰수

n,m = map(int,input().split())

a = list(map(int,input().split()))

res = set()

for i in range(n):
    for j in range(i+1 , n):
        for k in range(j+1 , n):
            res.add(a[i]+a[j]+a[k])

res = list(res)
res.sort(reverse=True)

print(res[m-1])
