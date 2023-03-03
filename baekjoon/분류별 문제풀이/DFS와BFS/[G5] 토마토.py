import sys
from collections import deque
# 움직일 수 있는 경우의 수
move = ((1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1))
# 인풋 최적화
input = sys.stdin.readline
# 가로, 세로, 높이
M, N, H = map(int,input().split())
# 박스
B = []
# 토마토들
T = []
# 안 익은 토마토 수
full = N*M*H
for i in range(H):
    li_h = []
    for j in range(N):
        li_n = list(map(int, input().split()))
        for k in range(M):
            # 익은 토마토
            if li_n[k] == 1:
                full-=1
                # 가로, 세로, 높이, 큐에서 사용할 카운트
                T.append((i,j,k,0))
            # 빈 곳
            elif li_n[k] == -1:
                full -= 1
        li_h.append(li_n)
    B.append(li_h)

# BFS
Q = deque(T)
while Q:
    z, y, x, c = Q.popleft()
    # 안 익은 토마토가 없는 경우. 큐의 제일 마지막 카운트가 답이다.
    if full == 0:
        print(Q[-1][-1] if Q else c)
        break
    for dz, dy, dx in move:
        nz, ny, nx = z+dz, y+dy, x+dx
        if 0<=nz<H and 0<=ny<N and 0<=nx<M and B[nz][ny][nx] == 0:
            B[nz][ny][nx] = 1
            full -= 1
            Q.append((nz,ny,nx,c + 1))
# break 문이 안 걸린 경우. 모두 익지 못하는 상황
else:
    print(-1)