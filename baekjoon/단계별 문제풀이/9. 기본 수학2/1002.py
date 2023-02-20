# 수학적인 사고와 계산이 필요하다. 일단 그려보면 쉽다
"""
결론부터 얘기하면, 두 원의 중심 사이의 거리(d)와 각 원의 반지름 길이(r1, r2)를 통해 두 원의 상태를 파악할 수 있다. 
d가 r1 r2합보다 크면, 원이 만나지 않는다. 
d가 r1 r2합과 같으면 한 곳에서 만난다.(외접)
d가 r1 r2 차보다 크면서, r1 r2합보다 작으면 두 곳에서 만난다.
d가 r1 r2 차와 같으면 한 곳에서 만난다.(내접) 
d가 r1 r2 차r1과 r2의 차가 d보다 크면서 r1과 r2의 합이 d보다 크면, 두 곳에서 만난다.
"""
from math import sqrt, pow
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = sqrt(pow(x1-x2, 2)+pow(y1-y2, 2))
    if d == 0 and r1 == r2:
        print(-1)
    elif abs(r1-r2) > d:
        print(0)
    elif abs(r1-r2) == d:
        print(1)
    elif abs(r1-r2) < d and d < r1+r2:
        print(2)
    elif d == r1+r2:
        print(1)
    elif d > r1+r2:
        print(0)
