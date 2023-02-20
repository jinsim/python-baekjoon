"""

"""
import sys
input=sys.stdin.readline
from collections import deque

# 행 열
R, C = map(int,input().split())
# 칸 이동
move = ((1,0), (-1,0), (0,1), (0,-1))
# 초기 지훈과 불 위치를 담을 변수들. 불은 여러개일 수 있다.
J_x = J_y = 0
fires = set()

# 미로 초기화. 불이 지나다니면서 maze의 내용을 변경시키므로 리스트 형식이어야 한다.
# F가 한 줄에 여러개일 수도 있으므로 2중 for문을 돌려서 인덱스를 저장한다.
maze = []
for i in range(R):
    word = list(input().rstrip())
    if 'J' in word:
        J_y = i
        J_x = word.index('J')
    if 'F' in word:
        for j in range(C):
            if word[j] == 'F':
                fires.add((i, j))
    maze.append(word)

# 큐 생성. 불이 먼저 지나가야 한다. 같은 차례에서 지훈이 먼저 지나가고 불이 겹치는 경우를 계산하기 어렵기 때문이다.
# y좌표, x좌표, 지훈인지 불인지, 몇번째 이동인지
Q = deque()
for F_y, F_x in fires:
    Q.append((F_y, F_x, 'F', 0))
Q.append((J_y, J_x, 'J', 0))

# ret이 변경되면 답이 나온 것이다.
ret = 0

# BFS.
while Q:
    if ret:
        break
    y, x, t, c = Q.popleft()
    for dy, dx in move:
        ny, nx = y + dy, x + dx
        # 불인 경우
        if t == 'F':
            if 0 <= ny < R and 0 <= nx < C:
                # 공간과 지훈으로 갈 수 있다. 도착한 후 maze를 F로 변경한다. (visited 역할)
                if maze[ny][nx] == '.' or maze[ny][nx] == 'J':
                    maze[ny][nx] = 'F'
                    Q.append((ny, nx, 'F', c+1))
        # 지훈인 경우
        else:
            # 칸 안에서 움직일 때는 공간만 갈 수 있다. 마찬가지로 maze를 J로 변경해야 재방문을 하지 않는다.
            if 0 <= ny < R and 0 <= nx < C:
                if maze[ny][nx] == '.':
                    maze[ny][nx] = 'J'
                    Q.append((ny, nx, 'J', c+1))
            else:
                ret = c+1

print(ret if ret else 'IMPOSSIBLE')