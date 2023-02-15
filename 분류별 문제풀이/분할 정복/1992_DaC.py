import sys
input = sys.stdin.readline

N = int(input())
video = []
for _ in range(N):
    video.append(input().rstrip())

# 이중 for문 빠른 탈출을 위해 함수로 선언
def check_video(y, x, size):
    checker = video[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if checker != video[i][j]:
                return False
    return checker

def zip_video(y, x, size):
    ret = check_video(y, x, size)
    if not check_video(y, x, size):
        size //= 2
        print("(", end='')
        zip_video(y, x, size)
        zip_video(y, x+size, size)
        zip_video(y+size, x, size)
        zip_video(y+size, x+size, size)
        print(")", end='')

    else:
        print(ret, end='')
zip_video(0, 0, N)




