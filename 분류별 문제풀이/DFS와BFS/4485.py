import heapq
import sys
input=sys.stdin.readline
INF=sys.maxsize

# 함수 선언(속도 개선)
def dijkstra(n):
    cave = [list(map(int, input().split())) for _ in range(n)]
    # 잃은 돈, y좌표, x좌표
    H = [(cave[0][0], 0, 0)]
    while H:
        m, y, x = heapq.heappop(H)
        # 답이 나온 경우에는 중단
        if y == n - 1 and x == n - 1:
            ret = m
            break
        for dy, dx in mv:
            ny, nx = y + dy, x + dx
            # 방문한 좌표를 -1로 설정하여 재방문 막기
            if 0 <= ny < n and 0 <= nx < n and cave[ny][nx] != -1:
                heapq.heappush(H, (m + cave[ny][nx], ny, nx))
                cave[ny][nx] = -1
    return ret

mv = ((1,0), (-1,0), (0,1), (0,-1))
cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0:
        break
    print(f"Problem {cnt}: {dijkstra(n)}")
