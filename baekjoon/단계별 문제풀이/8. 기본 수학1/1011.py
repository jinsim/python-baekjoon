# 직접 노트에 써보면서 하면 더욱 이해하기 쉽다.
"""
dis는 거리, n은 거리의 제곱근을 내림한 것, nn은 그 수를 다시 제곱한 것이다. 
거리에 따른 숫자를 직접 그려보면 이해가 쉬울 것이다.
"""
for _ in range(int(input())):
    a, b = map(int, input().split())
    dis = b-a
    n = int(dis**0.5)
    nn = n**2
    if dis < 4:
        print(dis)
    elif dis == nn:
        print(2*n-1)
    elif dis <= nn+n:
        print(2*n)
    else:
        print(2*n+1)
