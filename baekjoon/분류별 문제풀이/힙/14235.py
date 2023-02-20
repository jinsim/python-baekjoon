# 힙의 개념만 알면 풀 수 있는 문제.
from heapq import *
import sys
input = sys.stdin.readline
h = []
for i in range(int(input())):
    num = input()
    if num[0] != '0':
        gift = list(map(int, num.split()))
        for i in range(1, gift[0]+1):
            heappush(h, -gift[i])
    else:
        if h:
            print(-heappop(h))
        else: print(-1)
    