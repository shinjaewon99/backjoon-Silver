# 7785번


n = int(input())

arr = {}
for i in range(n):
    a , b = input().split()
    if b =='enter':
        arr[a] = ''
    
    elif b =='leave':
        del(arr[a])


for a in sorted(arr.keys(), reverse=True):
    print(a)
    


