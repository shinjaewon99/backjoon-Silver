# 2822번


arr = []
for i in range(8):
    arr.append(int(input()))


arr_sort = sorted(arr,reverse=True)

big = []

for j in range(5):
    big.append(arr_sort[j])

sum = 0

tmp = []

for k in big :
    sum +=k
    tmp.append(arr.index(k))

print(sum)

tmp_sort = sorted(tmp)

for p in tmp_sort:
    print(p+1 , end=' ')





    