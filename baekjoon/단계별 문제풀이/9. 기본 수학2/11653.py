# 그냥 풀면 아슬아슬하게 풀린다. 기준을 나누는 숫자에 두면 된다.
n = int(input())
num = []
for i in range(2, int(n**0.5)+1):
    while n % i == 0:
        n //= i
        num.append(i)
if n != 1:
    num.append(n)
print(*num, sep='\n')
