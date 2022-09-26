# 특정 거리의 도시 찾기(Good)
"""
다익스트라를 활용한 최단 거리 문제이다. heqp을 사용해서 풀이했다.
정점들에 대한 정보로 그래프 인접 리스트를 생성한다.
거리와 정점 정보를 넣는 힙을 생성하고, 출발 정점을 넣는다.
인접 리스트를 참고하여 연결된 노드들을 heap에 넣으면서 출발지로부터의 거리를 갱신한다.
이때, 이미 방문한 노드여서 최단 거리가 지정된 경우는 제외한다.
거리가 목표 거리에 도달하면, 최단 거리가 목표 거리인 노드들을 출력한다.  
"""
import heapq
import sys
import collections

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
distances = [sys.maxsize] * (n+1) # 출발 정점으로부터 거리. 최대값으로 생성해둔다.
distances[x] = 0 # 초기 정점을 0으로 설정한다.
ret = [] # 정답인 노드들을 모을 리스트

# 그래프 인접 리스트 생성
graph = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 힙 생성(거리, 정점)
Q = [(0, x)]

while Q:
    dist, node = heapq.heappop(Q)
    # 거리가 목표 거리보다 적으면, 그래프에서 도착 가능 정점들을 가져온다.
    if dist < k:
        for dest_node in graph[node]:
            # 현재까지 저장된 거리보다 짧을 때만 거리를 갱신하고 힙에 넣는다.
            if dist+1 < distances[dest_node]:
                distances[dest_node] = dist+1
                heapq.heappush(Q, (dist+1, dest_node))
    # 거리가 목표 거리에 도달하였으면, 최단 거리가 목표 거리인 노드만 ret에 더한다.
    else:
        if dist <= distances[node]:
            ret.append(node)

# 노드들을 오름차순으로 정렬 후 출력한다.
if ret:
    ret.sort()
    print(*ret, sep='\n')
else:
    print(-1)
