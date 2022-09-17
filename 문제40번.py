# 7785번

n = int(input())

person = {}

for i in range(n):
    p , c = input().split()

    if c == "enter":
        person[p] = "enter"
    else:
        if person[p]:
            del person[p]


for j in sorted(person, reverse=True):
    print(j)