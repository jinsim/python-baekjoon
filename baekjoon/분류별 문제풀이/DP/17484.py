"""
우주선이 갈 수 있는 경우를 계산하여 DP로 풀이하였다.
같은 방향으로 두번 연속 갈 수 없다는 조건을 만족하기 위해서, 직진하는 경우(0), 왼쪽에서 오는 경우(-1), 오른쪽에서 오는 경우(1)에서의 최솟값을 나눠서 저장하였다.
"""
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
space = []
for _ in range(N):
    space.append(list(map(lambda x: [int(x)]*3, input().split())))
for i in range(1, N):
    for j in range(M):
        # 직진하는 경우는 현재 위치 바로 위의 위치에서의 왼쪽 대각선, 오른쪽 대각선에 저장된 값의 최솟값을 더하면 된다.
        space[i][j][0] += min(space[i - 1][j][-1], space[i - 1][j][1])
        if j == 0:
            space[i][j][1] += min(space[i-1][j+1][-1], space[i-1][j+1][0])
            space[i][j][-1] = INF
        elif j == M-1:
            space[i][j][1] = INF
            space[i][j][-1] += min(space[i-1][j-1][1], space[i-1][j-1][0])
        else:
            space[i][j][1] += min(space[i - 1][j + 1][-1], space[i - 1][j + 1][0])
            space[i][j][-1] += min(space[i - 1][j - 1][1], space[i - 1][j - 1][0])
print(min(map(min,space[-1])))