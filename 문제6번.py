# 4673번


n = set(range(1,10001))
mv = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)

    mv.add(i)

n = n - mv

for k in sorted(n):
    print(k)