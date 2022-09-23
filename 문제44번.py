# 15904번

n = input()

arr = ['U' , 'C' , 'P' , 'C']

flag = True

for i in range(4):
    if arr[i] in n:
        flag = True
        index = n.find(arr[i])
        n = n[index+1::]

    else:
        flag = False
        break

if flag == True :
  print('I love UCPC')
else :
  print('I hate UCPC')