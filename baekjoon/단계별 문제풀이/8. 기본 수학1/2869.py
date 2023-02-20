"""
매일 a-b씩 오르는 것과 같다. 다만, 남은 길이가 b이하인 경우에는 그 직전 올라갈 때 끝까지 닿은 경우이므로, v-b가 기준이다. 
다만, 올림으로 구해야한다. ceil을 사용해도 되지만, 몫에 1을 뺀 후 다시 1을 더해 int로 버림을 할 수도 있다. 이유: 최소 단위가 1이라서.1
"""
import math
a, b, v = map(int, input().split())
print(math.ceil((v-b)/(a-b)))
# print(int(v-b-1)/(a-b)+1))

