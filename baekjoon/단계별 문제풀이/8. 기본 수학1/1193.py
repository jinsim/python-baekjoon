# 누적합
n = int(input())
val = i = 1 # val은 기준 값, i는 세로칸
while n > val:
    i += 1
    val += i
a = val-n+1
b = i-val+n
if i % 2 == 1:
    print(a, b, sep='/')
else:
    print(b, a, sep='/')
