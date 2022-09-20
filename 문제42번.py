# 5365번

arr = []
for i in range(int(input())):
    a,b,c,d = input().rstrip().split()
    b,c,d = map(int,(b,c,d))
    arr.append((d,c,b,a))
arr.sort()
print(arr[-1][3])
print(arr[0][3])