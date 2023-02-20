import sys

#표준입력을 파일로 설정
sys.stdin = open("../input.txt", "r")

N, M, L, K = map(int, input().split())
meteors = []
for _ in range(K):
    x, y = map(int, input().split())
    meteors.append((x, y))
# print(meteors)
meteors.sort()
print(meteors)
ret = 0
for i in range(K-1):
    for j in range(i+1, K):
        x1, y1 = meteors[i]
        x2, y2 = meteors[j]
        if x2 <= x1+L:
            if y1 >= y2 and y2 >= y1-L:
                ti, tx, ty = i, x1, y1
                cnt = 0
                while tx <= x1 + L:
                    if y2 <= ty and ty <= y2 + L:
                        cnt += 1
                    ti += 1
                    if ti == K:
                        break
                    tx, ty = meteors[ti]
                ret = max(cnt, ret)
            if y1 <= y2 and y2 <= y1+L:
                ti, tx, ty = i, x1, y1
                cnt = 0
                while tx <= x1 + L:
                    if y2 >= ty and ty >= y2 - L:
                        cnt += 1
                    ti += 1
                    if ti == K:
                        break
                    tx, ty = meteors[ti]
                ret = max(cnt, ret)
print(K-ret)