# 재귀의 개념을 확인하는 문제
def fibo(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibo(n-1)+fibo(n-2)

print(fibo(int(input())))
