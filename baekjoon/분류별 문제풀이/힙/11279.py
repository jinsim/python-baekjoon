# 힙의 개념만 알면 풀 수 있는 문제.
from heapq import *
import sys
input = sys.stdin.readline
h = []
for _ in range(int(input())):
    num = int(input())
    if num:
        heappush(h, -1*num)
    else:
        if h:
            print(-1*heappop(h))
        else: print(0)