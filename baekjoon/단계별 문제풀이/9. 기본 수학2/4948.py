# 미리 에라토스테네스의 체를 선언하면 빨리 끝난다.
"""
수의 범위인 123456의 2배만큼 리스트를 만든다. 
에라토스테네스의 체는, 2부터 리스트 끝 인덱스의 제곱근까지 중,
리스트에서 True인 값이 소수이므로 그 수의 곱들을 리스트에서 False로 변경한다.

이유 : 100까지의 수가 있을 때, 최댓값인 120을 제곱근하면 10.xxx가 나오고, 따라서 10보다 큰 두 수로 121을 만들 수 없다. 따라서 10까지만 반복문을 돌리면 된다. 
"""

from math import sqrt
num = 123456
prime = [0, 0]+[1]*(2*num-1)
for i in range(2, int(sqrt(2*num))+1):
    if prime[i]:
        for j in range(i*2, 2*num+1, i):
            prime[j] = 0
while True:
    n = int(input())
    if not n:
        break
    print(sum(prime[n+1:2*n+1]))
