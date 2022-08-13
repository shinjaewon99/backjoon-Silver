# 1181번


n = int(input())

arr = []

for i in range(n):
    arr.append(input())

set_arr = list(set(arr))


sort_arr =[]

for i in set_arr:
    sort_arr.append((len(i), i))


result = sorted(sort_arr)

for len_arr, arr in result:
    print(arr)