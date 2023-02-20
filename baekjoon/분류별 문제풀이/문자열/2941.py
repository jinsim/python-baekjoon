# 문제를 잘 이해해야한다.
l = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
for i in l:
    a = a.replace(i, '*')
print(len(a))
