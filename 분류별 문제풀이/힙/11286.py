# 힙의 구조만 알면 풀 수 있는 문제
from heapq import *
import sys
input = sys.stdin.readline
h = []
for _ in range(int(input())):
    num = int(input())
    if num:
        heappush(h, (abs(num), num))
    else:
        if h:
            print(heappop(h)[1])
        else: print(0)