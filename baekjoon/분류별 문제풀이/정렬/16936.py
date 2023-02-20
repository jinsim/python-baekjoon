# 문제에 대한 깊은 고민과 defaultdict 문법만 안다면 쉽게 풀 수 있다.
"""
우선 나3에서 3으로 나누어 떨어져야한다는 것이 포인트이다. 
모든 숫자들에게 3으로 최대한 나눌 수 있는 횟수를 구한 후에, 정렬하면 된다.
같은 횟수 사이에서는 곱2밖에 허용되지 않기 때문이다. 
따라서 숫자들을 오름차순으로 정렬한 후, 재귀를 이용해서 cnt를 하나씩 더해 넘기며 3으로 최대한 나눌 수 있는 횟수를 구한다. 
횟수를 키값으로 해서 defaultdict에 저장하고, Key를 기준으로 오름차순 정렬, ans에 연결해준다.
그리고 리스트를 출력하면 끝!
"""
from collections import defaultdict
dic = defaultdict(list) 
ans = []

def division(num, cnt):
    if num % 3 == 0:
        division(num//3, cnt+1)
    else: dic[cnt].append(num*(3**cnt))

input()
a = sorted(list(map(int, input().split())))

for i in a:
    division(i, 0)

for key, val in sorted(dic.items(), reverse=True):
    ans.extend(val)
    
print(*ans)