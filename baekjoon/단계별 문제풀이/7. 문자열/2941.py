# 난이도가 높다. 문제에서 무엇을 원하는지를 알아야한다.
l = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
for i in l:
    a = a.replace(i, '!')
print(len(a))
