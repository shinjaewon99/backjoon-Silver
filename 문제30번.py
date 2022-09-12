# 1652번

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(str,input())))


res = [0,0]
for j in range(n):
    cnt_a , cnt_b = 0,0
    for k in range(n):
        if arr[j][k] =='.':
            cnt_a +=1
        elif arr[j][k] =='X':
            if cnt_a >=2:
                res[0] +=1
            cnt_a =0

        if arr[k][j] =='.':
            cnt_b +=1
        elif arr[k][j] == 'X':
            if cnt_b >= 2:
                res[1] +=1
            cnt_b =0

    if k == n-1:
        if cnt_a >=2:
            res[0] +=1
        if cnt_b >=2 :
            res[1] +=1


print(' '.join(map(str,res)))

