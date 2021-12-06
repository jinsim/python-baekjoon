# 자릿수를 모두 더하는 방법, 집합 연산
def d(n):
    return i+sum(map(int, str(i)))

s = set()
t = range(1, 10001)
for i in t:
    s.add(d(i))
for i in sorted(set(t)-s):
    print(i)
