# [S1] 정수 삼각형
import sys
input = sys.stdin.readline

n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))

for i in range(n-1, 0, -1):
    for j in range(i):
        tmp = tri[i][j]
        if j != i:
            tmp = max(tri[i][j+1], tmp)
        tri[i-1][j] += tmp
print(tri[0][0])

