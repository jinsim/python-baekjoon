# [S1] RGB 거리
import sys
input = sys.stdin.readline
N = int(input())
moneys = []
for _ in range(N):
    moneys.append(list(map(int, input().split())))

for i in range(1, N):
    moneys[i][0] += min(moneys[i-1][1], moneys[i-1][2])
    moneys[i][1] += min(moneys[i-1][0], moneys[i-1][2])
    moneys[i][2] += min(moneys[i-1][0], moneys[i-1][1])
print(min(moneys[-1]))