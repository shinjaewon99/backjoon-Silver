# 2810번
n = int(input())
d = input()

count = 0

for i in range(len(d)):
    if d[i] == 'L':
        count +=1


if count == 0 :
    print(n)

else:
    print(n-(count//2-1))