# 1058번

n , m = map(int,input().split())

arr= []

res = [i for i  in range(1, n+1)]

total = 0

while res:

    total += m-1

    if total >= len(res):

        total %= len(res)

    
    arr.append(str(res.pop(total)))

print("<", ", ".join(arr), ">", sep="")
