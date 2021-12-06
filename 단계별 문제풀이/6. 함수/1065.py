# 조건에 집중하면 아래의 코드보다 더 쉽게 풀수도 있다.
def a(n):
    n = list(map(int, str(n)))
    l = len(n)
    if l > 1:
        k = n[1]-n[0]
    if l > 2:
        for i in range(2, l):
            if k != n[i]-n[i-1]:
                return 0
    return 1

num = 0
for i in range(1, int(input())+1):
    num += a(i)
print(num)
