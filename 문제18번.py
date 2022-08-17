# 1120번

a,b =input().split()

arr = []

for i in range(len(b)-len(a)+1):
    cnt =0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt +=1

    arr.append(cnt)

print(min(arr))