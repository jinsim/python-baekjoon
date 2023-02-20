from collections import deque
R, C = map(int,input().split())

# maze = [[0]*C for _ in range(R)]
maze = []

move = ((1,0), (-1,0), (0,1), (0,-1))
m = []
J_x = J_y = 0
fires = set()
# print(maze)
# for i in range(R):
#     word = input().replace('#','0').replace('.','1')
#     # print(word)
#     if 'J' in word:
#         J_y = i
#         J_x = word.index('J')
#         word = word.replace('J', '2')
#     if 'F' in word:
#         fires.add((i, word.index('F')))
#         word = word.replace('F', '0')
#     # print(word)
#     maze.append(list(map(int, list(word))))

# print(m, J_y, J_x, F_x, F_y)
# 세로, 가로, 속성
Q = deque()
Q.append((J_y, J_y, 'J'))
for F_y, F_x in fires:
    Q.append((F_y, F_x, 'F'))

# j의 수
j_cnt = 0

cnt = 0
ret = 0
while Q:
    if ret:
        break
    cnt+=1
    y, x, t = Q.popleft()
    print(y, x, t)
    for dy, dx in move:
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C:
            # print(ny, nx, maze[ny][nx])
            if t == 'J':
                if maze[ny][nx] == 1:
                    # print('성공')
                    if ny == 0 or nx == 0 or ny == R-1 or nx == C-1:
                        ret = cnt
                    Q.append((ny, nx, 'J'))
            else:
                if maze[ny][nx] != 0:
                    maze[ny][nx] = 0
                    Q.append((ny, nx, 'F'))
print(ret if ret else 'IMPOSSIBLE')
#             if t == '' and maze[ny][nx] == 'F':
#                 maze[ny][nx] = 'J'
#                 Q.append((ny, nx, 'J'))
#     return jihoon
# def jihoon(y, x):
#     jihoon = ()
#     for dy, dx in move:
#         ny, nx = y + dy, x + dx
#         if 0 < ny < R and 0 < nx < C:
#             if maze[ny][nx] == '.':
#                 maze[ny][nx] = 'J'
#                 jihoon.add((ny, nx))
#     return jihoon
# def fire(y, x):
#     fires = ()
#     for dy, dx in move:
#         ny, nx = y+dy, x+dx
#         if 0<ny<R and 0<nx<C:
#             if maze[ny][nx] == '.' or maze[ny][nx] == 'J':
#                 maze[ny][nx] = 'F'
#                 fires.add((ny, nx))
#     return fires
# fire(F_y, F_x)
#

