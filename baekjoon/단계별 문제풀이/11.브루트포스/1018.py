# 상당한 고민이 필요한 문제다.
"""
반복문은, 맨 위의 행부터 한 줄씩 줄어든다.(x) 이를 위해 deque를 사용한다.
그리고 행이 오른쪽에 하나씩 이동한다.(j)
이 과정으로 8x8의 체스판이 만들어지고, 비교를 시작하면 된다.

기준이 되는 체스판의 첫줄은
WBWBWBWB
BWBWBWBW
냐에 따라 2개로 나뉘고, 번갈아 반복된다. 
이것을 ret_a, ret_b로 파악하고, 줄이 변할 때마다 둘을 바꿔가며 일치할 때마다 하나씩 더해간다. 
이때, a에 일치하지 않으면 자연스럽게 a가 아닌 것과 일치한다.
한 줄이 지날 때마다 ret_a와 ret_b를 더한 합이 8인 것을 생각하면 쉬울 것이다. 

"""
from collections import deque
a = 'WB'*4
x, y = map(int, input().split())
li = deque()
for _ in range(x):
    li.append(input())

ret_a = ret_b = 0
ret = 64
ret_list = []
while x > 7:
    for j in range(y-7):
        for k in range(0, 8):
            for v in range(0, 8):
                if li[k][j+v] == a[v]:
                    ret_a += 1
                else:
                    ret_b += 1
            ret_a, ret_b = ret_b, ret_a
        ret_list.append(ret_a)
        ret_list.append(ret_b)
        ret_a = ret_b = 0
    x -= 1
    li.popleft()
print(min(ret_list))
