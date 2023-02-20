# 정렬 순서를 잘 생각해보면 된다. 
"""
반복되는 입력으로 인한 시간초과를 방지하기 위해서 input의 방식을 변경하였따. 
중복을 없애기 위해 set을 사용하였고, sort를 두번 사용하여 리스트를 정렬하였다.
순서는 일반적인 정렬 후에 len을 통한 정렬을 넣어 답을 낸다.
"""
import sys
input = sys.stdin.readline
l = []
for _ in range(int(input())):
    l.append(input().strip())
l = list(set(l))
l.sort()
l.sort(key=len)
# l.sort(key=lambda x: (len(x), x))
print(*l, sep='\n')
