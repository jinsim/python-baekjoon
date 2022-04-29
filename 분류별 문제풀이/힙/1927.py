# 힙의 개념만 알면 풀 수 있는 문제.
import heapq
import sys
input = sys.stdin.readline
h = []
for _ in range(int(input())):
    num = int(input())
    if num:
        heapq.heappush(h, num)
    else:
        if h:
            print(heapq.heappop(h))
        else: print(0)