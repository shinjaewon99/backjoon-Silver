# 9372번
# 신장 트리문제

import sys
input = sys.stdin.readline

a = int(input())

for _ in range(a):
    n, m = map(int, input().split())
    for _ in range(m):
        input() # 무조건 연결그래프이므로 입력 값을 무시한다.
    print(n - 1)