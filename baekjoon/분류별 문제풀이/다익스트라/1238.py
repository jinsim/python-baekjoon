"""
단방향, 다익스트라, 왕복, 각각의 도시에서 출발해서 가장 오래 걸린 시간 저장
방향을 반대로 돌려서 다익스트라를 실행하면 X로 오는 것도 한번에 처리 가능하다.
"""
import sys
import heapq
input = sys.stdin.readline

# 학생 수, 도로 수, 목적지
N, M, X = map(int, input().split())

f_roads = [[] for _ in range(N+1)]
r_roads = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t = list(map(int, input().split()))
    f_roads[a].append((b, t))
    r_roads[b].append((a, t))

def BFS(roads):
    # 출발 정점으로부터 비용. 최대값으로 생성해둔다.
    times = [sys.maxsize] * (N + 1)
    # 초기 정점을 0으로 설정한다.
    times[X] = 0

    Q = [(0, X)]

    while Q:
        time, node = heapq.heappop(Q)
        if time > times[node]:
            continue

        # 각 정점에서 들릴 수 있는 정점 중, 현재까지의 비용보다 더 적게 갈 수 있는 것만 채택한다.
        for dest_node, dest_time in roads[node]:
            new_time = time + dest_time
            # 비용을 갱신하고, 힙에 추가한다.
            if new_time < times[dest_node]:
                times[dest_node] = new_time
                heapq.heappush(Q, (new_time, dest_node))
    return times

f_times = BFS(f_roads)
r_times = BFS(r_roads)

ret = 0
for i in range(1, N+1):
    ret = max(ret, f_times[i]+r_times[i])
print(ret)



