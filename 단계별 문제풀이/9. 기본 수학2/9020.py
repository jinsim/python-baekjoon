# 에라토스테네스의 체를 활용한다. 
"""
ret과 n-ret을 사용해서 푸는 것을 추천한다.
"""
from math import sqrt
num = 10000
prime = [0, 0]+[1]*(num-1)
for i in range(2, int(sqrt(num))+1):
    if prime[i]:
        for j in range(i*2, num+1, i):
            prime[j] = 0

for _ in range(int(input())):
    n = int(input())
    ret = n//2
    while ret > 1:
        if prime[ret] and prime[n-ret]:
            break
        else:
            ret -= 1
    print(ret, n-ret)
