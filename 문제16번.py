# 15688번

import sys
 
n = int(sys.stdin.readline())
 
arr = []
 
for i in range(n):
    number = int(sys.stdin.readline())
    arr.append(number)
    

for j in sorted(arr):
    print(j)
