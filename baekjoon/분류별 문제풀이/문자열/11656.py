# 쉬운 문제다.
l = []
n = input()
for i in range(len(n)):
    l.append(n[i:])
print('\n'.join(sorted(l)))
