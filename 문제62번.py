# 카드 역배치



a = list(range(21))

for _ in range(10):
    n , m = map(int , input().split())
    for i in range((m-n+1)//2):
        a[n+i] , a[m-i] = a[m-i] , a[n+i]

a.pop(0)

for j in a:
    print(a, end=' ')
