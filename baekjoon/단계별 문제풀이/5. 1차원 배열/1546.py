# 람다는 선택. 이 경우는 오히려 총점에다가 한꺼번에 검사하는 게 더 빠르고 편함.
n = int(input())
l = list(map(int, input().split()))
m = max(l)
p = list(map(lambda x: x/m*100, l))
print(sum(p)/n)