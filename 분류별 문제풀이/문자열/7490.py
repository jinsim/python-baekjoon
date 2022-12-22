import sys

#표준입력을 파일로 설정
sys.stdin = open("../../input.txt","r")

n = int(input())
def cal(cal_exp):
    if not eval(cal_exp):
        print(cal_exp)
for _ in range(n):
    N = int(input())
    exp = ""
    for i in range(1, N+1):
        exp += str(i)
    print(exp)
    for i in range(1, N):

