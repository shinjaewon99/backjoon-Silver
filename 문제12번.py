# 10814번


n = int(input())
arr = []
for i in range(n):

    age, name =map(str, input().split())

    age = int(age)

    arr.append((age,name))



arr.sort(key = lambda a : (a[0]))
for a in arr:
    print(a[0],a[1])



# 람다란 : def temp(a):
#           return(a[0])
# 짝수를 판별하는 함수를 만든다고 했을때 일반함수는def is_even(x):  return x % 2 == 0이런식으로 표현을 할 수 있습니다.
# 이걸 람다로 표현하게 되면is_even = lambda x : x % 2 == 0이런식으로 표현할수 있습니다.





