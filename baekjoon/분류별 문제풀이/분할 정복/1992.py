import sys
import copy
import pprint

input = sys.stdin.readline

N = int(input())
video = []

for _ in range(N):
    video.append(input().rstrip())
# pprint.pprint(globals())
# pprint.pprint(locals())
def zip_video(n):
    global video
    tmp = [[]*n for _ in range(n)]
    for i in range(n):
        i *= 2
        for j in range(n):
            j *= 2
            if video[i][j] == video[i][j+1] == video[i+1][j] == video[i+1][j+1] and len(video[i][j]) == 1:
                tmp[i//2].append(video[i][j])
                pprint.pprint(locals())
                continue

            tmp[i//2].append('('+video[i][j]+video[i][j+1]+video[i+1][j]+video[i+1][j+1]+')')

            pprint.pprint(locals())
    video = copy.deepcopy(tmp)
    if n == 1:
        return
    zip_video(n//2)
if N == 1:
    print(*video)
else:
    zip_video(N//2)
    for i in video:
        print(*i, sep='', end='')
