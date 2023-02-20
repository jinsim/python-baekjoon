import sys

#표준입력을 파일로 설정
sys.stdin = open("../../input.txt","r")
input = sys.stdin.readline

while True:
    N = input().rstrip()
    if N == '0':
        break
    print("yes" if N == N[::-1] else "no")
