# 간단한 개념만 있으면 풀 수 있다.
def f(n):
    ret = 1
    if n > 1:
        ret = f(n-1)*n
    return ret

print(f(int(input())))
