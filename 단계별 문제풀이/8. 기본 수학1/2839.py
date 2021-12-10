# 브루트 포스로 풀 수도 있다.
"""
5 미만일 때의 예외처리를 해준 후, 5로 나눴을 때의 케이스에 따라 분류해주었다. 
while문을 돌리는 방식으로도 해결할 수 있따. 
""" 
n = int(input())
if n < 5 and n != 3:
    print(-1)
else:
    a = n//5
    b = n % 5
    if b == 0:
        print(a)
    elif b == 2:
        print(a+2 if a > 1 else -1)
    elif b == 4:
        print(a+2)
    else:
        print(a+1)
