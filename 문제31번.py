# 1834번

n = int(input())

total = 0

for i in range(n+1, n**2 , n+1):
    total +=i

print(total)