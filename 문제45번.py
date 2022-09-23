# 19939번


n , m =map(int,input().split())

if n < m * (m+1) // 2:
    print(-1)

else:
    flag = n - m*(m+1) //2
    if flag % m == 0:
        print(m - 1)
    else:
        print(m)