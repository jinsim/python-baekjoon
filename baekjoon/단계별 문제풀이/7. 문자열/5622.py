# 빨리 푸는 방식에 대한 고민. 필요에 의해 더미 데이터를 두는 것이 더 좋을 수도 있다. 
d = [3, 3, 3, 3, 3, 4, 3, 4]
n = 0
a = []
for i, v in enumerate(d):
    a+= [i+3]*v
for j in input():
    n +=a[ord(j)-65]
print(n)
    