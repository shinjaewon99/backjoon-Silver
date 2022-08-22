# 1822번

n = map(int,input().split())



a = set(map(int,input().split()))
b = set(map(int,input().split()))


print(len(a-b)) # 차집합의 길이를 출력

print(*sorted(list(a-b)))  # 차집합의 원소를 출력


