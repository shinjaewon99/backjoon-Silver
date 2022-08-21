# 2407번

from itertools import combinations
import math


n,m = map(int,input().split())

right = math.factorial(n)
left = (math.factorial(n-m)) * (math.factorial(m))



print(right//left)
