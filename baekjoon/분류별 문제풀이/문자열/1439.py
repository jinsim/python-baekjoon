# 쉬운 문제
n = input()
r = n[0]
ret = 0
for i in n:
    if i != r:
        ret += 1
        r = i
print((ret+1)//2)
