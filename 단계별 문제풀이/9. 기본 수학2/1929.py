# 시간 제한이 걸리는 문제. 최적화를 신경써야한다. 
import sys
from math import sqrt
a, b = map(int, sys.stdin.readline().split())

n = int(sqrt(b))
l = [0, 0]+[1]*(b-1)

for i in range(2, n+1):
    if l[i]:
        for j in range(i*2, b+1, i):
            l[j] = 0
            
for i in range(a, b+1):
    if l[i]:
        print(i)
