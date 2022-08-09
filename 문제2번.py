# 1316번


n = int(input())

total = n

for i in range(n):
    val = input()

    for j in range(len(val)-1):
        if val[j] == val[j+1]:
            pass
        elif val[j] in val[j+1::]:
            total -=1
            break


print(total)