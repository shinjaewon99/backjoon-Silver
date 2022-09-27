# 1026번

n = int(input())

alist = list(map(int,input().split()))
blist = list(map(int,input().split()))

sorta = sorted(alist, reverse=True)
sortb = sorted(blist)

total = 0
for i in range(n):

    total +=sorta[i] * sortb[i]

print(total)
