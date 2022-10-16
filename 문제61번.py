# 숫자만 추출(그 숫자의 소수도 출력)

from curses.ascii import isdigit


s = input()
res = 0
for i in s:
    if i.isdecimal():
        res = res *10 +int(i)

print(res)

cnt = 0
for j in range(1, res+1):
    if res%j == 0:
        cnt+=1

print(cnt)
